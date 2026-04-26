"""Configuration module for different package manager ecosystems."""

class EcosystemConfig:
    def __init__(self, name, out_dir, topics, official_orgs, known_buckets_urls, schemas):
        self.name = name
        self.out_dir = out_dir
        self.topics = topics
        self.official_orgs = official_orgs
        self.known_buckets_urls = known_buckets_urls
        self.schemas = schemas

def get_config(ecosystem_name):
    if ecosystem_name == "scoop_shovel":
        return EcosystemConfig(
            name="scoop_shovel",
            out_dir="scoop_shovel",
            topics=["scoop-bucket", "shovel-bucket"],
            official_orgs=["scoopinstaller", "ash258", "shovel-org"],
            known_buckets_urls={
                "scoop": "https://raw.githubusercontent.com/ScoopInstaller/Scoop/refs/heads/master/buckets.json",
                "shovel": "https://raw.githubusercontent.com/Ash258/Scoop-Core/refs/heads/main/buckets.json"
            },
            schemas={
                "scoop": "https://raw.githubusercontent.com/ScoopInstaller/Scoop/master/schema.json",
                "shovel": "https://raw.githubusercontent.com/Ash258/Scoop-Core/main/schema.json"
            }
        )
    elif ecosystem_name == "chocolatey":
        return EcosystemConfig(
            name="chocolatey",
            out_dir="chocolatey",
            topics=["chocolatey-packages", "chocolatey-automation", "chocolatey-repository", "chocolatey-community-repository", "chocolatey-automatic"],
            official_orgs=["chocolatey", "chocolatey-community"],
            known_buckets_urls={},
            schemas={}
        )
    else:
        raise ValueError(f"Unknown ecosystem: {ecosystem_name}")
