use anyhow::{Context, Result};
use chrono::{DateTime, TimeZone, Utc};
use clap::Parser;
use git2::{Oid, Repository, Sort, TreeWalkMode, TreeWalkResult};
use rayon::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::{HashMap, HashSet};
use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(long, default_value = "all")]
    ecosystem: String,
}

#[derive(Deserialize, Debug)]
struct AllJson {
    all: Vec<RepoEntry>,
}

#[derive(Deserialize, Debug)]
struct RepoEntry {
    full_name: String,
    git_url: String,
    #[serde(default)]
    topics: Vec<String>,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
struct Delta {
    added: usize,
    deleted: isize,
    retained: usize,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
struct DailyEntry {
    date: String,
    all: Delta,
    #[serde(skip_serializing_if = "Option::is_none")]
    scoop: Option<Delta>,
    #[serde(skip_serializing_if = "Option::is_none")]
    shovel: Option<Delta>,
}

struct Snapshot {
    all: HashSet<String>,
    scoop: HashSet<String>,
    shovel: HashSet<String>,
}

impl Snapshot {
    fn new() -> Self {
        Self {
            all: HashSet::new(),
            scoop: HashSet::new(),
            shovel: HashSet::new(),
        }
    }
}

fn calc_delta(curr: &HashSet<String>, prev: &HashSet<String>) -> Delta {
    let added = curr.difference(prev).count();
    let deleted = prev.difference(curr).count() as isize;
    let retained = curr.intersection(prev).count();
    Delta {
        added,
        deleted: -deleted,
        retained,
    }
}

fn get_daily_snapshots(
    repo_path: &Path,
    full_name: &str,
    is_shovel_bucket: bool,
    ecosystem: &str,
) -> Result<HashMap<String, Snapshot>> {
    let mut snapshots = HashMap::new();
    let today = Utc::now()
        .date_naive()
        .and_hms_opt(23, 59, 59)
        .unwrap()
        .and_utc();

    let mut dates = Vec::new();
    for i in (0..=91).rev() {
        let d = today - chrono::Duration::days(i);
        dates.push((d, d.format("%Y-%m-%d").to_string()));
    }

    let repo = Repository::open(repo_path)?;

    let mut revwalk = repo.revwalk()?;
    revwalk.push_head()?;
    revwalk.set_sorting(Sort::TIME)?;

    // Collect commits with their timestamps
    let mut commits = Vec::new();
    for oid in revwalk {
        if let Ok(oid) = oid {
            if let Ok(commit) = repo.find_commit(oid) {
                commits.push((commit.time().seconds(), oid));
            }
        }
    }

    for (d, date_str) in &dates {
        let timestamp = d.timestamp();

        let mut target_oid: Option<Oid> = None;
        for (commit_time, oid) in &commits {
            if *commit_time <= timestamp {
                target_oid = Some(*oid);
                break;
            }
        }

        let mut snap = Snapshot::new();

        if let Some(oid) = target_oid {
            if let Ok(commit) = repo.find_commit(oid) {
                if let Ok(tree) = commit.tree() {
                    // Walk the tree
                    tree.walk(TreeWalkMode::PreOrder, |root, entry| {
                        let name = match entry.name() {
                            Some(n) => n,
                            None => return TreeWalkResult::Ok,
                        };
                        let mut f = root.to_string();
                        f.push_str(name);

                        let f_lower = f.to_lowercase();

                        if ecosystem == "winget" {
                            if f.contains(".installer.") || f.contains(".locale.") {
                                return TreeWalkResult::Ok;
                            }
                            let normalized_f = f.replace("\\", "/");
                            if normalized_f.ends_with(".yaml") &&
                                (normalized_f.contains("manifests/") ||
                                 normalized_f.contains("packages/") ||
                                 normalized_f.contains("automatic/") ||
                                 normalized_f.contains("manual/"))
                            {
                                let parts: Vec<&str> = normalized_f.split('/').collect();
                                if let Some(last) = parts.last() {
                                    let item = format!("{}:{}", full_name.to_lowercase(), last.to_lowercase());
                                    snap.all.insert(item);
                                }
                            }
                        } else if f.ends_with(".json") || f.ends_with(".yaml") || f.ends_with(".yml") || f.ends_with(".nuspec") {
                            let normalized_f = f.replace("\\", "/");
                            let parts: Vec<&str> = normalized_f.split('/').collect();

                            if parts.len() == 1 || (parts.len() == 2 && parts[0] == "bucket") {
                                let recipe_name = parts.last().unwrap();
                                let item = format!("{}:{}", full_name.to_lowercase(), recipe_name.to_lowercase());

                                let is_shovel = is_shovel_bucket || f.ends_with(".yaml") || f.ends_with(".yml");

                                snap.all.insert(item.clone());
                                if ecosystem == "scoop_shovel" {
                                    if is_shovel {
                                        snap.shovel.insert(item);
                                    } else {
                                        snap.scoop.insert(item);
                                    }
                                }
                            } else if ecosystem == "chocolatey" {
                                // For chocolatey, allow deep structure like automatic/*/*.nuspec
                                if normalized_f.ends_with(".nuspec") {
                                    let recipe_name = parts.last().unwrap();
                                    let item = format!("{}:{}", full_name.to_lowercase(), recipe_name.to_lowercase());
                                    snap.all.insert(item);
                                }
                            }
                        }

                        TreeWalkResult::Ok
                    }).ok();
                }
            }
        }

        snapshots.insert(date_str.clone(), snap);
    }

    Ok(snapshots)
}

fn remove_readonly(path: &Path) {
    if let Ok(metadata) = fs::metadata(path) {
        let mut perms = metadata.permissions();
        perms.set_readonly(false);
        let _ = fs::set_permissions(path, perms);
    }
}

fn force_remove_dir_all(path: &Path) {
    let _ = fs::remove_dir_all(path);
    if path.exists() {
        // Fallback for Windows
        let _ = Command::new("cmd")
            .args(&["/C", "rmdir", "/S", "/Q", path.to_str().unwrap()])
            .status();
    }
}

fn process_repository(repo_entry: &RepoEntry, ecosystem: &str) -> Result<HashMap<String, Snapshot>> {
    let full_name = &repo_entry.full_name;
    let git_url = &repo_entry.git_url;
    let is_shovel_bucket = repo_entry.topics.contains(&"shovel-bucket".to_string());

    let safe_name = full_name.replace('/', "+");
    let repo_dir = PathBuf::from("../../temp_seed_clones").join(&safe_name);

    println!("[*] Seeding {}...", full_name);

    if repo_dir.exists() {
        let status = Command::new("git")
            .args(&["pull", "--quiet"])
            .current_dir(&repo_dir)
            .status();

        if status.is_err() || !status.unwrap().success() {
            println!("[!] Failed to pull {}, attempting fresh clone...", full_name);
            force_remove_dir_all(&repo_dir);
        }
    }

    if !repo_dir.exists() {
        let shallow_date = (Utc::now() - chrono::Duration::days(100)).format("%Y-%m-%d").to_string();
        let status = Command::new("git")
            .args(&["clone", "--quiet", &format!("--shallow-since={}", shallow_date), git_url, repo_dir.to_str().unwrap()])
            .status();

        if status.is_err() || !status.unwrap().success() {
            println!("[!] Shallow clone failed for {}, attempting full clone...", full_name);
            let status = Command::new("git")
                .args(&["clone", "--quiet", git_url, repo_dir.to_str().unwrap()])
                .status();

            if status.is_err() || !status.unwrap().success() {
                println!("[!] Failed to clone {}", full_name);
                return Err(anyhow::anyhow!("Clone failed"));
            }
        }
    }

    let snapshots = get_daily_snapshots(&repo_dir, full_name, is_shovel_bucket, ecosystem)?;

    // Cleanup
    force_remove_dir_all(&repo_dir);

    Ok(snapshots)
}

fn seed_ecosystem(ecosystem_name: &str) -> Result<()> {
    println!("\n{}\n[*] Starting seed generation for: {}\n{}", "=".repeat(50), ecosystem_name, "=".repeat(50));

    // Paths are relative to the rust executable which is inside scripts/seed_generator
    let root_dir = PathBuf::from("../..");
    let json_path = root_dir.join(ecosystem_name).join("all.json");

    if !json_path.exists() {
        println!("[!] {} not found. Run the crawler first.", json_path.display());
        return Ok(());
    }

    let json_str = fs::read_to_string(&json_path)?;
    let all_json: AllJson = serde_json::from_str(&json_str)?;

    if all_json.all.is_empty() {
        println!("[!] No repositories found in {}.", json_path.display());
        return Ok(());
    }

    let temp_dir = root_dir.join("temp_seed_clones");
    let _ = fs::create_dir_all(&temp_dir);

    let today = Utc::now().date_naive().and_hms_opt(23, 59, 59).unwrap().and_utc();
    let mut dates = Vec::new();
    for i in (0..=91).rev() {
        let d = today - chrono::Duration::days(i);
        dates.push(d.format("%Y-%m-%d").to_string());
    }

    // Process repositories in parallel
    let repo_snapshots: Vec<_> = all_json.all.par_iter()
        .filter_map(|repo| {
            process_repository(repo, ecosystem_name)
                .map_err(|e| println!("[!] Exception processing {}: {}", repo.full_name, e))
                .ok()
        })
        .collect();

    let mut global_snapshots: HashMap<String, Snapshot> = HashMap::new();
    for date_str in &dates {
        global_snapshots.insert(date_str.clone(), Snapshot::new());
    }

    for snaps in repo_snapshots {
        for (date_str, snap) in snaps {
            if let Some(global_snap) = global_snapshots.get_mut(&date_str) {
                global_snap.all.extend(snap.all);
                if ecosystem_name == "scoop_shovel" {
                    global_snap.scoop.extend(snap.scoop);
                    global_snap.shovel.extend(snap.shovel);
                }
            }
        }
    }

    let mut timeseries = Vec::new();
    for i in 1..dates.len() {
        let curr_date = &dates[i];
        let prev_date = &dates[i - 1];

        let curr_snap = global_snapshots.get(curr_date).unwrap();
        let prev_snap = global_snapshots.get(prev_date).unwrap();

        let mut daily_entry = DailyEntry {
            date: curr_date.clone(),
            all: calc_delta(&curr_snap.all, &prev_snap.all),
            scoop: None,
            shovel: None,
        };

        if ecosystem_name == "scoop_shovel" {
            daily_entry.scoop = Some(calc_delta(&curr_snap.scoop, &prev_snap.scoop));
            daily_entry.shovel = Some(calc_delta(&curr_snap.shovel, &prev_snap.shovel));
        }

        timeseries.push(daily_entry);
    }

    let seed_output_path = root_dir.join(ecosystem_name).join("seed_timeseries.json");
    let json_out = serde_json::to_string_pretty(&timeseries)?;
    fs::write(&seed_output_path, json_out)?;

    println!("[*] Seed generation complete. Timeseries rebuilt for last {} days. Saved to {}", timeseries.len(), seed_output_path.display());

    force_remove_dir_all(&temp_dir);

    Ok(())
}

fn main() -> Result<()> {
    let args = Args::parse();

    let ecosystems = if args.ecosystem == "all" {
        vec!["scoop_shovel", "chocolatey", "winget"]
    } else {
        vec![args.ecosystem.as_str()]
    };

    for eco in ecosystems {
        seed_ecosystem(eco)?;
    }

    Ok(())
}
