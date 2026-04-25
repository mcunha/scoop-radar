# scoop-radar
A data-driven, automated discovery and ranking engine for the Scoop package manager ecosystem on Windows

# Build Status
![Tests & Linting](https://github.com/mcunha/scoop-radar/actions/workflows/test.yml/badge.svg)
![Update Scoop Radar README](https://github.com/mcunha/scoop-radar/actions/workflows/update.yml/badge.svg)

# Acknowledgements
This project was heavily inspired by the original `awesome-scoop` directories maintained by [algomaniac](https://github.com/algomaniac) and [tapannallan](https://github.com/tapannallan).

# 📊 Ecosystem Health
* **Total Unique Recipes**: 6408
* **Ecosystem Auto-Update Health**: 83.07%
* **Ecosystem Reliability**: 91.6% (Sampled URL Health)
* **Official vs. Community**: 0 Official / 6408 Community
* **Bucket Ecosystem**: 489 Scoop / 4 Shovel
* **Bucket Graveyard (Stale > 1 Year)**: 🪦 151

### Ecosystem Growth (All Recipes)
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="growth_all_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="growth_all_light.svg">
  <img alt="All Recipes Growth" src="growth_all_light.svg">
</picture>

### Scoop vs Shovel Growth
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_scoop_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_scoop_light.svg">
    <img alt="Scoop Recipes Growth" src="growth_scoop_light.svg" width="49%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_shovel_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_shovel_light.svg">
    <img alt="Shovel Recipes Growth" src="growth_shovel_light.svg" width="49%">
  </picture>
</p>

# 🚀 Getting Started
To add and use any of the buckets listed below, simply run the following command in your terminal:
```powershell
scoop bucket add <bucket-name> <bucket-url>
```
For example, to add a specific bucket, find its URL from the list below and run:
```powershell
scoop bucket add my-awesome-bucket https://github.com/user/my-awesome-bucket
```
After adding the bucket, you can install any of its applications like this:
```powershell
scoop install my-awesome-bucket/<app-name>
```

# Third party buckets by popularity


## 💎 Hidden Gems
These buckets are actively maintained and feature a high percentage of **unique** applications not found in official repositories. Great for discovering niche tools!


### [wwvl/Scoop-Cursor](https://github.com/wwvl/Scoop-Cursor)
*   **Unique Recipes:** 288 (100.0% unique)
*   **Total Recipes:** 288

### [gdm257/scoop-257](https://github.com/gdm257/scoop-257)
*   **Unique Recipes:** 192 (100.0% unique)
*   **Total Recipes:** 192

### [Jadeiin/scoop](https://github.com/Jadeiin/scoop)
*   **Unique Recipes:** 190 (100.0% unique)
*   **Total Recipes:** 190

### [tomcdj71/scoop-dev-apps](https://github.com/tomcdj71/scoop-dev-apps)
*   **Unique Recipes:** 146 (100.0% unique)
*   **Total Recipes:** 146

### [ptbwu/dango](https://github.com/ptbwu/dango)
*   **Unique Recipes:** 141 (100.0% unique)
*   **Total Recipes:** 141

### [Capella87/capella-bucket](https://github.com/Capella87/capella-bucket)
*   **Unique Recipes:** 119 (100.0% unique)
*   **Total Recipes:** 119

### [tomcdj71/scoop-essential-apps](https://github.com/tomcdj71/scoop-essential-apps)
*   **Unique Recipes:** 113 (100.0% unique)
*   **Total Recipes:** 113

### [davidxuang/scoop-type](https://github.com/davidxuang/scoop-type)
*   **Unique Recipes:** 113 (100.0% unique)
*   **Total Recipes:** 113

### [huangnauh/carrot](https://github.com/huangnauh/carrot)
*   **Unique Recipes:** 113 (100.0% unique)
*   **Total Recipes:** 113

### [magicedy/scoop-bucket-m](https://github.com/magicedy/scoop-bucket-m)
*   **Unique Recipes:** 107 (100.0% unique)
*   **Total Recipes:** 107





## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.

<details>
<summary><b>Click to expand 489 Scoop buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |

| **[wwvl/Scoop-Cursor](directory/wwvl+Scoop-Cursor.md)** | 📦 288 | ⭐ 1.0 | 🔄 0% |  |

| **[gdm257/scoop-257](directory/gdm257+scoop-257.md)** | 📦 192 | ⭐ 1.0 | 🔄 90% |  |

| **[Jadeiin/scoop](directory/Jadeiin+scoop.md)** | 📦 190 | ⭐ 1.0 | 🔄 99% |  |

| **[tomcdj71/scoop-dev-apps](directory/tomcdj71+scoop-dev-apps.md)** | 📦 146 | ⭐ 1.0 | 🔄 88% |  |

| **[ptbwu/dango](directory/ptbwu+dango.md)** | 📦 141 | ⭐ 1.0 | 🔄 89% |  |

| **[Capella87/capella-bucket](directory/Capella87+capella-bucket.md)** | 📦 119 | ⭐ 1.0 | 🔄 96% |  |

| **[tomcdj71/scoop-essential-apps](directory/tomcdj71+scoop-essential-apps.md)** | 📦 113 | ⭐ 1.0 | 🔄 97% |  |

| **[davidxuang/scoop-type](directory/davidxuang+scoop-type.md)** | 📦 113 | ⭐ 1.0 | 🔄 100% |  |

| **[huangnauh/carrot](directory/huangnauh+carrot.md)** | 📦 113 | ⭐ 1.0 | 🔄 99% |  |

| **[magicedy/scoop-bucket-m](directory/magicedy+scoop-bucket-m.md)** | 📦 107 | ⭐ 1.0 | 🔄 91% |  |

| **[zeldrisho/scoop-bucket](directory/zeldrisho+scoop-bucket.md)** | 📦 106 | ⭐ 1.0 | 🔄 97% |  |

| **[jqk/scoopbucket](directory/jqk+scoopbucket.md)** | 📦 100 | ⭐ 1.0 | 🔄 82% |  |

| **[cesaryuan/scoop-cesar](directory/cesaryuan+scoop-cesar.md)** | 📦 92 | ⭐ 1.0 | 🔄 82% |  |

| **[WantChane/doge_bucket](directory/WantChane+doge_bucket.md)** | 📦 88 | ⭐ 1.0 | 🔄 99% |  |

| **[souhaiebtar/scoop-apps](directory/souhaiebtar+scoop-apps.md)** | 📦 86 | ⭐ 1.0 | 🔄 93% |  |

| **[lewis-yeung/scoop-bucket](directory/lewis-yeung+scoop-bucket.md)** | 📦 85 | ⭐ 1.0 | 🔄 86% |  |

| **[ZhangTianrong/scoop-bucket](directory/ZhangTianrong+scoop-bucket.md)** | 📦 82 | ⭐ 1.0 | 🔄 93% |  |

| **[Donaldduck8/malware-analysis-bucket](directory/Donaldduck8+malware-analysis-bucket.md)** | 📦 80 | ⭐ 1.0 | 🔄 69% |  |

| **[KnotUntied/scoop-knotuntied](directory/KnotUntied+scoop-knotuntied.md)** | 📦 77 | ⭐ 1.0 | 🔄 82% |  |

| **[huxiaoning/scoop_bucket](directory/huxiaoning+scoop_bucket.md)** | 📦 70 | ⭐ 1.0 | 🔄 83% |  |

| **[qwerty12/scoop-alts](directory/qwerty12+scoop-alts.md)** | 📦 60 | ⭐ 1.0 | 🔄 78% |  |

| **[li-ruijie/scoop](directory/li-ruijie+scoop.md)** | 📦 59 | ⭐ 1.0 | 🔄 100% |  |

| **[mvrpl/windows-apps](directory/mvrpl+windows-apps.md)** | 📦 53 | ⭐ 1.0 | 🔄 94% |  |

| **[LaelLuo/scoop](directory/LaelLuo+scoop.md)** | 📦 52 | ⭐ 1.0 | 🔄 100% |  |

| **[suquiya/suquiya_bucket](directory/suquiya+suquiya_bucket.md)** | 📦 47 | ⭐ 1.0 | 🔄 96% |  |

| **[apeiraco/scoop-bucket](directory/apeiraco+scoop-bucket.md)** | 📦 46 | ⭐ 1.0 | 🔄 96% |  |

| **[nateify/scoop-nateify](directory/nateify+scoop-nateify.md)** | 📦 46 | ⭐ 1.0 | 🔄 96% |  |

| **[MMKubicki/ScoopBucket](directory/MMKubicki+ScoopBucket.md)** | 📦 43 | ⭐ 1.0 | 🔄 100% |  |

| **[wanstarge/scoopx](directory/wanstarge+scoopx.md)** | 📦 42 | ⭐ 1.0 | 🔄 93% |  |

| **[niceEli/Pail](directory/niceEli+Pail.md)** | 📦 41 | ⭐ 1.0 | 🔄 93% |  |

| **[Spiraster/scoop-bucket](directory/Spiraster+scoop-bucket.md)** | 📦 41 | ⭐ 1.0 | 🔄 93% |  |

| **[Jastmaskerrr/Rojem-Scoop](directory/Jastmaskerrr+Rojem-Scoop.md)** | 📦 41 | ⭐ 1.0 | 🔄 95% |  |

| **[ypxun/scoop_bucket](directory/ypxun+scoop_bucket.md)** | 📦 41 | ⭐ 1.0 | 🔄 100% |  |

| **[kt-devhub/extra](directory/kt-devhub+extra.md)** | 📦 45 | ⭐ 1.0 | 🔄 89% |  |

| **[joaoricarte/jr-bucket](directory/joaoricarte+jr-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 95% |  |

| **[matracey/scoop-bucket](directory/matracey+scoop-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 100% |  |

| **[leic4u/Scoop-Store](directory/leic4u+Scoop-Store.md)** | 📦 38 | ⭐ 1.0 | 🔄 97% |  |

| **[jbwfu/scoop-bucket](directory/jbwfu+scoop-bucket.md)** | 📦 38 | ⭐ 1.0 | 🔄 97% |  |

| **[Lutra-Fs/scoop-bucket](directory/Lutra-Fs+scoop-bucket.md)** | 📦 38 | ⭐ 1.0 | 🔄 95% |  |

| **[NSPC911/le-bucket](directory/NSPC911+le-bucket.md)** | 📦 37 | ⭐ 1.0 | 🔄 97% |  |

| **[Strappazzon/scoop](directory/Strappazzon+scoop.md)** | 📦 36 | ⭐ 1.0 | 🔄 100% |  |

| **[issaclin32/scoop-bucket](directory/issaclin32+scoop-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 68% |  |

| **[maoyeedy/Scoop](directory/maoyeedy+Scoop.md)** | 📦 35 | ⭐ 1.0 | 🔄 94% |  |

| **[raisercostin/raiser-scoop-bucket](directory/raisercostin+raiser-scoop-bucket.md)** | 📦 34 | ⭐ 1.0 | 🔄 76% |  |

| **[MagicalDrizzle/scoop-personal](directory/MagicalDrizzle+scoop-personal.md)** | 📦 33 | ⭐ 1.0 | 🔄 79% |  |

| **[janlindblom/scoops](directory/janlindblom+scoops.md)** | 📦 33 | ⭐ 1.0 | 🔄 58% |  |

| **[nicerloop/scoop-nicerloop](directory/nicerloop+scoop-nicerloop.md)** | 📦 32 | ⭐ 1.0 | 🔄 62% |  |

| **[Zevan770/scoop_zev](directory/Zevan770+scoop_zev.md)** | 📦 32 | ⭐ 1.0 | 🔄 91% |  |

| **[ppyv/scoop-jp-fonts](directory/ppyv+scoop-jp-fonts.md)** | 📦 33 | ⭐ 1.0 | 🔄 100% |  |

| **[mslxl/ScoopIt](directory/mslxl+ScoopIt.md)** | 📦 36 | ⭐ 1.0 | 🔄 92% |  |

| **[LucasOe/scoop-lucasoe](directory/LucasOe+scoop-lucasoe.md)** | 📦 33 | ⭐ 1.0 | 🔄 97% |  |

| **[jat001/scoop-ox](directory/jat001+scoop-ox.md)** | 📦 38 | ⭐ 1.0 | 🔄 100% |  |

| **[icecreamZeng/scoop-bucket](directory/icecreamZeng+scoop-bucket.md)** | 📦 29 | ⭐ 1.0 | 🔄 66% |  |

| **[tac091/scoop-multi](directory/tac091+scoop-multi.md)** | 📦 31 | ⭐ 1.0 | 🔄 87% |  |

| **[Bergbok/Scoop-Bucket](directory/Bergbok+Scoop-Bucket.md)** | 📦 28 | ⭐ 1.0 | 🔄 68% |  |

| **[gigberg/localbucket](directory/gigberg+localbucket.md)** | 📦 28 | ⭐ 1.0 | 🔄 75% |  |

| **[amano41/scoop-bucket](directory/amano41+scoop-bucket.md)** | 📦 27 | ⭐ 1.0 | 🔄 96% |  |

| **[rodrigost23/scoop-bucket](directory/rodrigost23+scoop-bucket.md)** | 📦 26 | ⭐ 1.0 | 🔄 96% |  |

| **[pasze888/scoop-keepass](directory/pasze888+scoop-keepass.md)** | 📦 26 | ⭐ 1.0 | 🔄 100% |  |

| **[notPlancha/bucket](directory/notPlancha+bucket.md)** | 📦 29 | ⭐ 1.0 | 🔄 100% |  |

| **[yurical/scoop-mint](directory/yurical+scoop-mint.md)** | 📦 29 | ⭐ 1.0 | 🔄 97% |  |

| **[cmontage/scoopbucket-soup](directory/cmontage+scoopbucket-soup.md)** | 📦 28 | ⭐ 1.0 | 🔄 100% |  |

| **[Hayxi/Soap](directory/Hayxi+Soap.md)** | 📦 24 | ⭐ 1.0 | 🔄 96% |  |

| **[jonisb/Misc-scoops](directory/jonisb+Misc-scoops.md)** | 📦 23 | ⭐ 1.0 | 🔄 100% |  |

| **[ous50/ous50-bucket](directory/ous50+ous50-bucket.md)** | 📦 23 | ⭐ 1.0 | 🔄 96% |  |

| **[artiga033/Armory](directory/artiga033+Armory.md)** | 📦 22 | ⭐ 1.0 | 🔄 86% |  |

| **[filip2cz/scoop-retro](directory/filip2cz+scoop-retro.md)** | 📦 47 | ⭐ 1.0 | 🔄 2% |  |

| **[strxnge-effects/scoopert](directory/strxnge-effects+scoopert.md)** | 📦 21 | ⭐ 1.0 | 🔄 71% |  |

| **[KO6FCH/scoop-ham](directory/KO6FCH+scoop-ham.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[bodrick/scoop-bucket](directory/bodrick+scoop-bucket.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[crisipa/scoopbucket](directory/crisipa+scoopbucket.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[Dott-rus/apps](directory/Dott-rus+apps.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[phnthnhnm/Scoop](directory/phnthnhnm+Scoop.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[amorphobia/ScoopMirrored](directory/amorphobia+ScoopMirrored.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[plutotree/scoop-bucket](directory/plutotree+scoop-bucket.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[danalec/scoop-alts](directory/danalec+scoop-alts.md)** | 📦 18 | ⭐ 1.0 | 🔄 89% |  |

| **[ltguillaume/schep](directory/ltguillaume+schep.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[MoonWX/scoop_bucket](directory/MoonWX+scoop_bucket.md)** | 📦 17 | ⭐ 1.0 | 🔄 100% |  |

| **[touhoured/ScoopBucket](directory/touhoured+ScoopBucket.md)** | 📦 17 | ⭐ 1.0 | 🔄 94% |  |

| **[warthurton/scoop-ntwind](directory/warthurton+scoop-ntwind.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[cainiao1992/scoop-chenxf](directory/cainiao1992+scoop-chenxf.md)** | 📦 17 | ⭐ 1.0 | 🔄 100% |  |

| **[tkit1994/scoop_bucket](directory/tkit1994+scoop_bucket.md)** | 📦 16 | ⭐ 1.0 | 🔄 100% |  |

| **[petlyh/scoop-bucket](directory/petlyh+scoop-bucket.md)** | 📦 16 | ⭐ 1.0 | 🔄 44% |  |

| **[Snowflyt/snowforge](directory/Snowflyt+snowforge.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[bughug/scoop](directory/bughug+scoop.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[prettycation/margin](directory/prettycation+margin.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[nikkoura/scoop-bucket-elitedangerous](directory/nikkoura+scoop-bucket-elitedangerous.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[hmerritt/scoop-bucket](directory/hmerritt+scoop-bucket.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[kltk/scoop-bucket](directory/kltk+scoop-bucket.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[haomingz/scoop-bucket](directory/haomingz+scoop-bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 100% |  |

| **[kanami09/Scoop-xPack](directory/kanami09+Scoop-xPack.md)** | 📦 14 | ⭐ 1.0 | 🔄 57% |  |

| **[sbklb1/scoop-bucket](directory/sbklb1+scoop-bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 77% |  |

| **[Edenwize/scoop-apps](directory/Edenwize+scoop-apps.md)** | 📦 13 | ⭐ 1.0 | 🔄 46% |  |

| **[santarl/scoop_bucket](directory/santarl+scoop_bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 86% |  |

| **[ddavness/scoop-roblox](directory/ddavness+scoop-roblox.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[WenSimEHRP/OpenTTD-bucket](directory/WenSimEHRP+OpenTTD-bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[ifvlaboratory/ScoopBucket-ifvlab](directory/ifvlaboratory+ScoopBucket-ifvlab.md)** | 📦 12 | ⭐ 1.0 | 🔄 83% |  |

| **[JotmKKmkLTzE/Scoop-apps](directory/JotmKKmkLTzE+Scoop-apps.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[baaamn/Scoopercalifragilisticexpialidocious](directory/baaamn+Scoopercalifragilisticexpialidocious.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[swxfe/miscbucket](directory/swxfe+miscbucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[Jojo4GH/scoop-JojoIV](directory/Jojo4GH+scoop-JojoIV.md)** | 📦 11 | ⭐ 1.0 | 🔄 91% |  |

| **[jack-mil/scoop-bucket](directory/jack-mil+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[nostorg/scoop-nostr](directory/nostorg+scoop-nostr.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[pierreteam/scoop-js-engine](directory/pierreteam+scoop-js-engine.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[kenjiwho/scoop-bucket](directory/kenjiwho+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[ycrack/scoop-ycrack](directory/ycrack+scoop-ycrack.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[lucaspimentel/scoop-bucket](directory/lucaspimentel+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[warthurton/scoop-misc](directory/warthurton+scoop-misc.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[nonperforming/scoop-godot](directory/nonperforming+scoop-godot.md)** | 📦 12 | ⭐ 1.0 | 🔄 0% |  |

| **[bbkane/scoop-bucket](directory/bbkane+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 0% |  |

| **[insomnimus/scoop-bucket](directory/insomnimus+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[Vodes/Bucket](directory/Vodes+Bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[narnaud/scoop-bucket](directory/narnaud+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[chrismeller/scoop-bucket](directory/chrismeller+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[muxinxy/scoop-bucket](directory/muxinxy+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[MahdiAkrami01/scoop-bucket](directory/MahdiAkrami01+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[haukuen/endless](directory/haukuen+endless.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[Virakal/ScoopBucket](directory/Virakal+ScoopBucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[guitarrapc/scoop-bucket](directory/guitarrapc+scoop-bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[NECOtype/dip](directory/NECOtype+dip.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[pynappo/scoop-bucket](directory/pynappo+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[rsteube/scoop-bucket](directory/rsteube+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[jonz94/scoop-personal](directory/jonz94+scoop-personal.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[henshouse/scoop](directory/henshouse+scoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 88% |  |

| **[Nevuly/frostbite](directory/Nevuly+frostbite.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[urihcim/scoop-urihcim](directory/urihcim+scoop-urihcim.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[fahim-ahmed05/scoop-bucket](directory/fahim-ahmed05+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[AndreiVernon/scoop-cone](directory/AndreiVernon+scoop-cone.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[AureateGarden/Zeo-Apps](directory/AureateGarden+Zeo-Apps.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[RuiNtD/my-scoop-bucket](directory/RuiNtD+my-scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[BinToss/scoop-bucket](directory/BinToss+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[YDX-2147483647/scoop-bucket](directory/YDX-2147483647+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[yi-Xu-0100/scoop-bucket](directory/yi-Xu-0100+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |

| **[dyuu7/docket](directory/dyuu7+docket.md)** | 📦 10 | ⭐ 1.0 | 🔄 80% |  |

| **[zhangchaoza/scoop-extensions-bucket](directory/zhangchaoza+scoop-extensions-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 80% |  |

| **[Bennett-Yang/benckets](directory/Bennett-Yang+benckets.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[kengwang/scoop-bucket-kw](directory/kengwang+scoop-bucket-kw.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[back-lacking/personal-scoop](directory/back-lacking+personal-scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 29% |  |

| **[john180/scoop-bucket](directory/john180+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[bharatvaj/scoop-based](directory/bharatvaj+scoop-based.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[lkhrs/eve-tools](directory/lkhrs+eve-tools.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[stasjok/my-scoop-bucket](directory/stasjok+my-scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[RemySkye/RemyScoop](directory/RemySkye+RemyScoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 43% |  |

| **[felixmaker/scoop-felixmaker](directory/felixmaker+scoop-felixmaker.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[Deskehs/personalBucket](directory/Deskehs+personalBucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[robinovitch61/scoop-bucket](directory/robinovitch61+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[Exterminate5573/ScoopBucket](directory/Exterminate5573+ScoopBucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[mtpdx/scoop-bucket](directory/mtpdx+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[SwingURM/scoop_bucket](directory/SwingURM+scoop_bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[sammary114/self-custom](directory/sammary114+self-custom.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[qwjyh/scoop_bucket](directory/qwjyh+scoop_bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[BoringBoredom/scoop-bucket](directory/BoringBoredom+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[schmitzCatz/awesome-scoop-bucket](directory/schmitzCatz+awesome-scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/unity3d](directory/tree-s+unity3d.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[zhangfeiran/mybucket](directory/zhangfeiran+mybucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 50% |  |

| **[j1g5awi/scoop-jigsaw](directory/j1g5awi+scoop-jigsaw.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[endowdly/endo-scoop](directory/endowdly+endo-scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 71% |  |

| **[go-feature-flag/scoop](directory/go-feature-flag+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 0% |  |

| **[0x0003/0x0003-s-bucket](directory/0x0003+0x0003-s-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[SnowSquire/scoop](directory/SnowSquire+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[Fleafa/myBucket](directory/Fleafa+myBucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[bgsulz/bgsulz-Bucket](directory/bgsulz+bgsulz-Bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 60% |  |

| **[aliesbelik/astro](directory/aliesbelik+astro.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[pact-foundation/scoop](directory/pact-foundation+scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 0% |  |

| **[hrshtst/scoop-bucket](directory/hrshtst+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[scowalt/scoop-apps](directory/scowalt+scoop-apps.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[amreus/bucket](directory/amreus+bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[coatl-dev/scoop-coatl-dev](directory/coatl-dev+scoop-coatl-dev.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[gitfool/scoop-vpinball](directory/gitfool+scoop-vpinball.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[loustact/locket](directory/loustact+locket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[mistyrosetta/mistyscoop](directory/mistyrosetta+mistyscoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[goark/scoop-bucket](directory/goark+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[Velgus/Scoop-Velgus](directory/Velgus+Scoop-Velgus.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[arrow2nd/scoop-bucket](directory/arrow2nd+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[emotion3459/Bucket](directory/emotion3459+Bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[NoPlagiarism/noplag](directory/NoPlagiarism+noplag.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[iliqiliev/iliya-bucket](directory/iliqiliev+iliya-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[WyvernIXTL/stupid-bucket](directory/WyvernIXTL+stupid-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[schnow265/scoopet](directory/schnow265+scoopet.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[kaweezle/scoop-bucket](directory/kaweezle+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 0% |  |

| **[quardbreak/scoop-bucket](directory/quardbreak+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[sunfkny/scoop-bucket](directory/sunfkny+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[Dumpinground/expert-eureka](directory/Dumpinground+expert-eureka.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[wtbxsjy/mattress](directory/wtbxsjy+mattress.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[Koalhack/SCrispyBucket](directory/Koalhack+SCrispyBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 71% |  |

| **[zknx/scoop-bucket](directory/zknx+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[DenisionSoft/scoop-box](directory/DenisionSoft+scoop-box.md)** | 📦 5 | ⭐ 1.0 | 🔄 40% |  |

| **[itsHardStyl3r/scoop-personal](directory/itsHardStyl3r+scoop-personal.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[filip2cz/scoop-installers](directory/filip2cz+scoop-installers.md)** | 📦 4 | ⭐ 1.0 | 🔄 50% |  |

| **[Animesh-Ghosh/kulfi-scoop](directory/Animesh-Ghosh+kulfi-scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[Ziyph/Scoop](directory/Ziyph+Scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[mitoteam/scoop-bucket](directory/mitoteam+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[Zalk0/ZalkosBucket](directory/Zalk0+ZalkosBucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[DeltaLaboratory/lemon](directory/DeltaLaboratory+lemon.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[Yukari0201/scoop-bucket](directory/Yukari0201+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[eclecticbouquet/pail](directory/eclecticbouquet+pail.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[qiazo/scoop-bucket](directory/qiazo+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[somaz94/scoop-bucket](directory/somaz94+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[Deaquay/scoop-bucket](directory/Deaquay+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[rfnash/scoop](directory/rfnash+scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[peterrichards-lr/scoop-bucket](directory/peterrichards-lr+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[tech189/tech189-bucket](directory/tech189+tech189-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[JHXs/MyBucket](directory/JHXs+MyBucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[indra87g/awesome-indonesia-dev](directory/indra87g+awesome-indonesia-dev.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[fredjoseph/scoop-bucket](directory/fredjoseph+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 88% |  |

| **[zandercodes/scoop-pangolin](directory/zandercodes+scoop-pangolin.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ShihaoShenDev/ScoopBucket](directory/ShihaoShenDev+ScoopBucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[vladhietala/vlad-scoop-bucket](directory/vladhietala+vlad-scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[jbangdev/scoop-bucket](directory/jbangdev+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[ba230t/scoop-bucket](directory/ba230t+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/arc](directory/tree-s+arc.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/windowsSDK](directory/tree-s+windowsSDK.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[max-sn/personal-bucket](directory/max-sn+personal-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[toddyoe/scoop-canary](directory/toddyoe+scoop-canary.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[t-mart/bucket](directory/t-mart+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[xiongnemo/windows-binaries-scoop-bucket](directory/xiongnemo+windows-binaries-scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[xavidop/scoop-bucket](directory/xavidop+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Hzbeta/scoop-zephyr](directory/Hzbeta+scoop-zephyr.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Nerixyz/silly-bucket](directory/Nerixyz+silly-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[TechPro424/scoop-bucket](directory/TechPro424+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[madLinux7/scoop-bucket](directory/madLinux7+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[70sh1/jug](directory/70sh1+jug.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[gildas/scoop-bucket](directory/gildas+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tbnguyen1407/scoop-bucket](directory/tbnguyen1407+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[FriesI23/scoop-bucket](directory/FriesI23+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[babarot/scoop-bucket](directory/babarot+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[kemokemo/scoop-bucket](directory/kemokemo+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 0% |  |

| **[sbolch/ScoopV](directory/sbolch+ScoopV.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[damienbutt/scoop-bucket](directory/damienbutt+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[nzbr/scoop-bucket](directory/nzbr+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[speratus/redot-engine-bucket](directory/speratus+redot-engine-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[perryhq/perryhq-scoop](directory/perryhq+perryhq-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[cppbear/scoop-cppbear](directory/cppbear+scoop-cppbear.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[amrbashir/scoop-bucket](directory/amrbashir+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ArmoryNode/PersonalScoopBucket](directory/ArmoryNode+PersonalScoopBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[SamTherapy/scoop](directory/SamTherapy+scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[ddanielsantos/dd-bucket](directory/ddanielsantos+dd-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[Mufi-Lang/mufi-bucket](directory/Mufi-Lang+mufi-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[nightshadecf/scoop-bucket](directory/nightshadecf+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ClaudiaHeart/scoop-bucket-claudiaheart](directory/ClaudiaHeart+scoop-bucket-claudiaheart.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[OmyDaGreat/MaleficBucket](directory/OmyDaGreat+MaleficBucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[auth0/scoop-auth0-cli](directory/auth0+scoop-auth0-cli.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[psmux/scoop-psmux](directory/psmux+scoop-psmux.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[rustfs/scoop-bucket](directory/rustfs+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/virtualbox](directory/tree-s+virtualbox.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[kdash-rs/scoop-kdash](directory/kdash-rs+scoop-kdash.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ipatalas/scoop-bucket](directory/ipatalas+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[kubri/scoop-bucket](directory/kubri+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[mohitmishra786/scoop-bucket](directory/mohitmishra786+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Nimblesite/scoop-bucket](directory/Nimblesite+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[systempromptio/scoop-bucket](directory/systempromptio+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[RTF22/scoop-vocix](directory/RTF22+scoop-vocix.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[monkescience/scoop-bucket](directory/monkescience+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ionos-cloud/scoop-bucket](directory/ionos-cloud+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[AChep/keyguard-repo-scoop](directory/AChep+keyguard-repo-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Gildedter/scoop-bucket](directory/Gildedter+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[BobH-Official/bobh-scoop-bucket](directory/BobH-Official+bobh-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ysthakur/my-scoop-extras](directory/ysthakur+my-scoop-extras.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[prskr/scoop-the-prancing-package](directory/prskr+scoop-the-prancing-package.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[TheRealOwenJ/LimeAndLemon](directory/TheRealOwenJ+LimeAndLemon.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[geekifier/underscoop](directory/geekifier+underscoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[emilio-toledo/scoop-bucket](directory/emilio-toledo+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tokentopapp/scoop-tokentop](directory/tokentopapp+scoop-tokentop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[louiss0/the-code-fixer-23-buckets](directory/louiss0+the-code-fixer-23-buckets.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[debugtheworldbot/scoop-keystats](directory/debugtheworldbot+scoop-keystats.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[macleod-ee/scoop](directory/macleod-ee+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[terraform-docs/scoop-bucket](directory/terraform-docs+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ecsdeployer/scoop-bucket](directory/ecsdeployer+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[henrygd/beszel-scoops](directory/henrygd+beszel-scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[xhorntail/xho-scoops](directory/xhorntail+xho-scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[nareshnavinash/scoop-bucket](directory/nareshnavinash+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[dev-tonholo/scoop-svg-to-compose](directory/dev-tonholo+scoop-svg-to-compose.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[stefanlogue/scoops](directory/stefanlogue+scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[PranavU-Coder/scoop-bucket](directory/PranavU-Coder+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[timrabl/scoop-bucket](directory/timrabl+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[shoehorn-dev/scoop-bucket](directory/shoehorn-dev+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[yazeed/scoop-bucket-proc](directory/yazeed+scoop-bucket-proc.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[voicemeet/scoop-bucket](directory/voicemeet+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[mlm-games/buckets-scoop](directory/mlm-games+buckets-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[sebastianappelberg/scoop-bucket](directory/sebastianappelberg+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[caffeine-addictt/scoop-bucket](directory/caffeine-addictt+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[mthmulders/scoop-mcs](directory/mthmulders+scoop-mcs.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[danielealbano/scoop-mcp-tools](directory/danielealbano+scoop-mcp-tools.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Gasoid/baker-scoop](directory/Gasoid+baker-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[wsgtcyx/PDF-zusammenfuegen-scoop](directory/wsgtcyx+PDF-zusammenfuegen-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/GBStudio](directory/tree-s+GBStudio.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[DoveBoy/Scoop-Bucket](directory/DoveBoy+Scoop-Bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[roma-glushko/scoop-tango](directory/roma-glushko+scoop-tango.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[sarub0b0/scoop-bucket](directory/sarub0b0+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[nikkoura/scoop-bucket-vkb](directory/nikkoura+scoop-bucket-vkb.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[WenSimEHRP/wenmisc-bucket](directory/WenSimEHRP+wenmisc-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 20% |  |

| **[sohamw03/Scoop-Bucket](directory/sohamw03+Scoop-Bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[StasysMusial/scoop-bucket](directory/StasysMusial+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[dom1torii/cs2](directory/dom1torii+cs2.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[rafalohaki/oofscoop](directory/rafalohaki+oofscoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Bedingled403/scoop-cool](directory/Bedingled403+scoop-cool.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[004Ongoro/scoop-bucket](directory/004Ongoro+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[leonismoe/scoop-bucket](directory/leonismoe+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[belleradh/birdbucket](directory/belleradh+birdbucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ultimateanu/homebrew-software](directory/ultimateanu+homebrew-software.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[wenmin92/scoop-wenmin92](directory/wenmin92+scoop-wenmin92.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[ypurpl/bucket](directory/ypurpl+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[cmvanb/scoop-bucket](directory/cmvanb+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[sbolch/ScoopZed](directory/sbolch+ScoopZed.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Lelio88/he-bucket](directory/Lelio88+he-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[meenzen/scoop](directory/meenzen+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[yanghanlin/orihime-first](directory/yanghanlin+orihime-first.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[tree-s/mIRC](directory/tree-s+mIRC.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[evg4b/scoop-bucket](directory/evg4b+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aisair/scoop-bucket](directory/aisair+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ankddev/scoop-ankddev](directory/ankddev+scoop-ankddev.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[nettracex/nettracex-bucket](directory/nettracex+nettracex-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[nginx/scoop-bucket](directory/nginx+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[dh6wk/ScoopRepo](directory/dh6wk+ScoopRepo.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[rayun56/scoop-bucket](directory/rayun56+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[rocketblend/scoop-bucket](directory/rocketblend+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Overimagine1/Poop](directory/Overimagine1+Poop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[jazzwang/scoop-bucket](directory/jazzwang+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[ldez/scoop-bucket](directory/ldez+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[txyyh/Scoop](directory/txyyh+Scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[jahanbani/scoop-anaconda3](directory/jahanbani+scoop-anaconda3.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[SunsetMkt/scoop-aliceincradle](directory/SunsetMkt+scoop-aliceincradle.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[QZLin/winscp-trans](directory/QZLin+winscp-trans.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Absolucy/scoop-lucy](directory/Absolucy+scoop-lucy.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[varabyte/scoop-varabyte](directory/varabyte+scoop-varabyte.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Qile0317/compbio-scoop-bucket](directory/Qile0317+compbio-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Shivelight/scoop-bucket](directory/Shivelight+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[OnlyF0uR/blockchain](directory/OnlyF0uR+blockchain.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Humorist7336/bucket](directory/Humorist7336+bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Der-Floh/scoop-bucket](directory/Der-Floh+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Excalian/scoop](directory/Excalian+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[luke-beep/azrael-scoop](directory/luke-beep+azrael-scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 0% |  |

| **[KhoiCanDev/scoop-vietnamese-softwares-bucket](directory/KhoiCanDev+scoop-vietnamese-softwares-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 33% |  |

| **[Cooperter/scoop-bucket](directory/Cooperter+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[Bennett-Yang/bencket](directory/Bennett-Yang+bencket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[wind-mask/scoop-bucket-repository](directory/wind-mask+scoop-bucket-repository.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[bacnh85/scoop-bucket](directory/bacnh85+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[jo12bar/scoop-bucket](directory/jo12bar+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Elypha/garden](directory/Elypha+garden.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[Desdaemon/scoop-repo](directory/Desdaemon+scoop-repo.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[lisonge/scoop-ls](directory/lisonge+scoop-ls.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[rnine/scoop-duobolt](directory/rnine+scoop-duobolt.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[wriftai/scoop-bucket](directory/wriftai+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[MichaelHaussmann/scoop-play](directory/MichaelHaussmann+scoop-play.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[tinymce/scoop-bucket](directory/tinymce+scoop-bucket.md)** | 📦 69 | ⭐ 1.0 | 🔄 100% |  |

| **[Orphoros/scoop-bucket](directory/Orphoros+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[skiletro/scoop-vr-software-bucket](directory/skiletro+scoop-vr-software-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[siketyan/scoop-bucket](directory/siketyan+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[h-takesg/h-takesg_bucket](directory/h-takesg+h-takesg_bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[x-idian/scoop-bucket](directory/x-idian+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[DubskySteam/scoop-bucket](directory/DubskySteam+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[kevinboss/maple](directory/kevinboss+maple.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[trdthg/scoop-bucket](directory/trdthg+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[phanirithvij/scop](directory/phanirithvij+scop.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[SKalt/scoop-git-cc](directory/SKalt+scoop-git-cc.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ZhenyuXiao/toolbox](directory/ZhenyuXiao+toolbox.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[heroku-miraheze/scoop-bucket](directory/heroku-miraheze+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[SunsetMkt/scoop-vlmcsd](directory/SunsetMkt+scoop-vlmcsd.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/progressquest](directory/tree-s+progressquest.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[rakkateichou/rakbucket](directory/rakkateichou+rakbucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tlipoca9/scoop-bucket](directory/tlipoca9+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[nonperforming/scoop](directory/nonperforming+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aeswibon/scoop-bucket](directory/aeswibon+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[jwt-rs/scoop-jwt-ui](directory/jwt-rs+scoop-jwt-ui.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[upyun/carrot](directory/upyun+carrot.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[elenakrittik/bucket](directory/elenakrittik+bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[darkliquid/bucket](directory/darkliquid+bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Jenway/scoop](directory/Jenway+scoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[negative-authentication/NegativeAuthBucket](directory/negative-authentication+NegativeAuthBucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[onsamyj/dipper](directory/onsamyj+dipper.md)** | 📦 9 | ⭐ 1.0 | 🔄 56% |  |

| **[Daniele-rolli/Beaver-Bucket](directory/Daniele-rolli+Beaver-Bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Dreista/scoop-bucket](directory/Dreista+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[GunMoe/scoop-bucket](directory/GunMoe+scoop-bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 69% |  |

| **[shrlion/F-one](directory/shrlion+F-one.md)** | 📦 9 | ⭐ 1.0 | 🔄 89% |  |

| **[Dumpinground/openra-mods](directory/Dumpinground+openra-mods.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Dumpinground/emulator-tools](directory/Dumpinground+emulator-tools.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[DelineaXPM/scoop-bucket](directory/DelineaXPM+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Nriver/Scoop-Nriver](directory/Nriver+Scoop-Nriver.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/shiftcrypto](directory/tree-s+shiftcrypto.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[aklinovitskiy/scoop-bucket](directory/aklinovitskiy+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 50% |  |

| **[syrinka/scoop](directory/syrinka+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[Sectly/scoop-bucket](directory/Sectly+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[FrostyNick/scoop-bucket](directory/FrostyNick+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[myksmstk/scoop-myks-public](directory/myksmstk+scoop-myks-public.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[Kyure-A/ksb](directory/Kyure-A+ksb.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[herouu/scoop_bucket](directory/herouu+scoop_bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[sirredbeard/determined-bucket](directory/sirredbeard+determined-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[anderlli0053/Staging](directory/anderlli0053+Staging.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[cOborski/chartreuse-triceratops](directory/cOborski+chartreuse-triceratops.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[ncruces/scoop](directory/ncruces+scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[elliot40404/elliot](directory/elliot40404+elliot.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[rexlManu/scoop-bucket](directory/rexlManu+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Notenoughusernames/bluemoon](directory/Notenoughusernames+bluemoon.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[tree-s/fraps](directory/tree-s+fraps.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[acdzh/zpt](directory/acdzh+zpt.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[skellygore/scoop-bucket](directory/skellygore+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[MANICX100/scoop](directory/MANICX100+scoop.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[foosel/scoop-bucket](directory/foosel+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[burgr033/burgrBucket](directory/burgr033+burgrBucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[subchen/scoop-bucket](directory/subchen+scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[jlaasonen/scoop-bucket](directory/jlaasonen+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Vechro/ryence](directory/Vechro+ryence.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[dem2k/scoop-bucket](directory/dem2k+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[miketvo/scoop-miketvo](directory/miketvo+scoop-miketvo.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[TronicLabs/troniclabs-buckets](directory/TronicLabs+troniclabs-buckets.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[sebagomez/scoopbucket](directory/sebagomez+scoopbucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[jihuayu/jscoop](directory/jihuayu+jscoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[arcturegulus/scoop](directory/arcturegulus+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Madh93/scoop-bucket](directory/Madh93+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[gaojr/MyScoopBucket](directory/gaojr+MyScoopBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Alveel/scoop-bucket](directory/Alveel+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[sveltinio/scoop-sveltin](directory/sveltinio+scoop-sveltin.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[wiuri/wr_scoop_bucket](directory/wiuri+wr_scoop_bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Shemnei/scoop-bucket](directory/Shemnei+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[celsiusnarhwal/kirigiri](directory/celsiusnarhwal+kirigiri.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Skyppex/sky-bucket](directory/Skyppex+sky-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[edavidaja/scoop-bucket](directory/edavidaja+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[tejasraman/Konsole-Scoop](directory/tejasraman+Konsole-Scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[thesilvercraft/SilverCraftBucket](directory/thesilvercraft+SilverCraftBucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[ereborstudios/scoop-bucket](directory/ereborstudios+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[hjjhjj/doraemon-bucket](directory/hjjhjj+doraemon-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[Aldebaranoro/scoop-bucket](directory/Aldebaranoro+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[comp500/scoop-comp500](directory/comp500+scoop-comp500.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Logiase/scoop-embedded](directory/Logiase+scoop-embedded.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[pvarentsov/scoop-iola](directory/pvarentsov+scoop-iola.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[littleli/scoop-garage](directory/littleli+scoop-garage.md)** | 📦 31 | ⭐ 1.0 | 🔄 77% |  |

| **[rkolka/scoop-manifold](directory/rkolka+scoop-manifold.md)** | 📦 9 | ⭐ 1.0 | 🔄 56% |  |

| **[pgollangi/scoop-bucket](directory/pgollangi+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[gfieldGG/bucket](directory/gfieldGG+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[flvinny/scoop-bucket](directory/flvinny+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[JManch/scoop-bucket](directory/JManch+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[xfournet/scoop-sboot](directory/xfournet+scoop-sboot.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tkishiro/ScoopBucket](directory/tkishiro+ScoopBucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[adamrodger/scoop-bucket](directory/adamrodger+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[backd-io/scoop-bucket](directory/backd-io+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Dumpinground/themes](directory/Dumpinground+themes.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[uxiew/scoop-fruit](directory/uxiew+scoop-fruit.md)** | 📦 7 | ⭐ 1.0 | 🔄 57% |  |

| **[EscWasTaken/scoop-special](directory/EscWasTaken+scoop-special.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[Saw-mon-and-Natalie/scoop-crypto](directory/Saw-mon-and-Natalie+scoop-crypto.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[arnos-stuff/arnos-scoop-bucket](directory/arnos-stuff+arnos-scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[TonyZYT2000/scoop-Andromeda](directory/TonyZYT2000+scoop-Andromeda.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[pasoevi/more-scoops](directory/pasoevi+more-scoops.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[studoot/my-scoop-bucket](directory/studoot+my-scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[zhangfeiran/my-bucket](directory/zhangfeiran+my-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[daekma/scoop-bucket](directory/daekma+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[mvietri/scoop-hela](directory/mvietri+scoop-hela.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[nimzo6689/Scoop-nimzo6689](directory/nimzo6689+Scoop-nimzo6689.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Duckle29/duckles_bucket](directory/Duckle29+duckles_bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[fioepq9/scoop-aqua](directory/fioepq9+scoop-aqua.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[cidertool/scoop-bucket](directory/cidertool+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[gpailler/scoop-apps](directory/gpailler+scoop-apps.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[vsviridov/scoop-bucket](directory/vsviridov+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[sambeckingham/dhall](directory/sambeckingham+dhall.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Kazanami/zeus-bucket](directory/Kazanami+zeus-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 60% |  |

| **[CALMorACT/hola_bucket](directory/CALMorACT+hola_bucket.md)** | 📦 18 | ⭐ 1.0 | 🔄 83% |  |

| **[tclog/scoop-tclog](directory/tclog+scoop-tclog.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[GreatGodApollo/trough](directory/GreatGodApollo+trough.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Dumpinground/simulator-tools](directory/Dumpinground+simulator-tools.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[fire/scoop-fire](directory/fire+scoop-fire.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[AndreasBrostrom/arma3-scoop-bucket](directory/AndreasBrostrom+arma3-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[jku1995/Jbucket](directory/jku1995+Jbucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[s-oram/bento](directory/s-oram+bento.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[brad-jones/scoop-bucket](directory/brad-jones+scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 0% |  |

| **[pigsflew/scoop-arbitrariae](directory/pigsflew+scoop-arbitrariae.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[garyng/scoop-garyng](directory/garyng+scoop-garyng.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[roose/scoop-tools](directory/roose+scoop-tools.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[prantlf/scoop-bucket](directory/prantlf+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[devcsrj/scoop-bucket](directory/devcsrj+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Etsinshao/scoop-bucket](directory/Etsinshao+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[colkey/scoop-colkey](directory/colkey+scoop-colkey.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[PorridgePi/scoop-bucket](directory/PorridgePi+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[filippobuletto/pot-pourri](directory/filippobuletto+pot-pourri.md)** | 📦 7 | ⭐ 1.0 | 🔄 57% |  |

| **[leonidboykov/scoop-bucket](directory/leonidboykov+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Master-Hash/bucket](directory/Master-Hash+bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[yukihane/scoop-bucket-yukihane](directory/yukihane+scoop-bucket-yukihane.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aenthill/scoop-bucket](directory/aenthill+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[icedream/scoop-bucket](directory/icedream+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[FDUZS/spoon](directory/FDUZS+spoon.md)** | 📦 42 | ⭐ 1.0 | 🔄 98% |  |

| **[TheAsuro/scoop-stuff](directory/TheAsuro+scoop-stuff.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Kantouzin/scoop-bucketouzin](directory/Kantouzin+scoop-bucketouzin.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[nickbudi/scoop-bucket](directory/nickbudi+scoop-bucket.md)** | 📦 30 | ⭐ 1.0 | 🔄 80% |  |

| **[earnestma/scoop-earne](directory/earnestma+scoop-earne.md)** | 📦 10 | ⭐ 1.0 | 🔄 70% |  |

| **[Br1ght0ne/scoop-bucket](directory/Br1ght0ne+scoop-bucket.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[mogeko/scoop-bucket](directory/mogeko+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[Mushus/scoop-bucket](directory/Mushus+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[tobyvin/scoop-tobyvin](directory/tobyvin+scoop-tobyvin.md)** | 📦 25 | ⭐ 1.0 | 🔄 72% |  |

| **[Harakku/harakkus-scoop-bucket](directory/Harakku+harakkus-scoop-bucket.md)** | 📦 21 | ⭐ 1.0 | 🔄 86% |  |

| **[ProfElements/EmulatorBucket](directory/ProfElements+EmulatorBucket.md)** | 📦 27 | ⭐ 1.0 | 🔄 0% |  |

| **[zt-luo/bucket-luo](directory/zt-luo+bucket-luo.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |


</details>

## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.

<details>
<summary><b>Click to expand 4 Shovel buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |

| **[caoli5288/scoop-bucket](directory/caoli5288+scoop-bucket.md)** | 📦 25 | ⭐ 1.0 | 🔄 84% |  |

| **[Siphalor/scoop-bucket](directory/Siphalor+scoop-bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 100% |  |

| **[dearrrfish/scoop-bucket](directory/dearrrfish+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[Jeddunk/scoop-bucket](directory/Jeddunk+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |


</details>

## 📦 All Known Buckets
A combined list of every bucket discovered in the ecosystem.

<details>
<summary><b>Click to expand all 493 discovered buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |

| **[wwvl/Scoop-Cursor](directory/wwvl+Scoop-Cursor.md)** | 📦 288 | ⭐ 1.0 | 🔄 0% |  |

| **[gdm257/scoop-257](directory/gdm257+scoop-257.md)** | 📦 192 | ⭐ 1.0 | 🔄 90% |  |

| **[Jadeiin/scoop](directory/Jadeiin+scoop.md)** | 📦 190 | ⭐ 1.0 | 🔄 99% |  |

| **[tomcdj71/scoop-dev-apps](directory/tomcdj71+scoop-dev-apps.md)** | 📦 146 | ⭐ 1.0 | 🔄 88% |  |

| **[ptbwu/dango](directory/ptbwu+dango.md)** | 📦 141 | ⭐ 1.0 | 🔄 89% |  |

| **[Capella87/capella-bucket](directory/Capella87+capella-bucket.md)** | 📦 119 | ⭐ 1.0 | 🔄 96% |  |

| **[tomcdj71/scoop-essential-apps](directory/tomcdj71+scoop-essential-apps.md)** | 📦 113 | ⭐ 1.0 | 🔄 97% |  |

| **[davidxuang/scoop-type](directory/davidxuang+scoop-type.md)** | 📦 113 | ⭐ 1.0 | 🔄 100% |  |

| **[huangnauh/carrot](directory/huangnauh+carrot.md)** | 📦 113 | ⭐ 1.0 | 🔄 99% |  |

| **[magicedy/scoop-bucket-m](directory/magicedy+scoop-bucket-m.md)** | 📦 107 | ⭐ 1.0 | 🔄 91% |  |

| **[zeldrisho/scoop-bucket](directory/zeldrisho+scoop-bucket.md)** | 📦 106 | ⭐ 1.0 | 🔄 97% |  |

| **[jqk/scoopbucket](directory/jqk+scoopbucket.md)** | 📦 100 | ⭐ 1.0 | 🔄 82% |  |

| **[cesaryuan/scoop-cesar](directory/cesaryuan+scoop-cesar.md)** | 📦 92 | ⭐ 1.0 | 🔄 82% |  |

| **[WantChane/doge_bucket](directory/WantChane+doge_bucket.md)** | 📦 88 | ⭐ 1.0 | 🔄 99% |  |

| **[souhaiebtar/scoop-apps](directory/souhaiebtar+scoop-apps.md)** | 📦 86 | ⭐ 1.0 | 🔄 93% |  |

| **[lewis-yeung/scoop-bucket](directory/lewis-yeung+scoop-bucket.md)** | 📦 85 | ⭐ 1.0 | 🔄 86% |  |

| **[ZhangTianrong/scoop-bucket](directory/ZhangTianrong+scoop-bucket.md)** | 📦 82 | ⭐ 1.0 | 🔄 93% |  |

| **[Donaldduck8/malware-analysis-bucket](directory/Donaldduck8+malware-analysis-bucket.md)** | 📦 80 | ⭐ 1.0 | 🔄 69% |  |

| **[KnotUntied/scoop-knotuntied](directory/KnotUntied+scoop-knotuntied.md)** | 📦 77 | ⭐ 1.0 | 🔄 82% |  |

| **[huxiaoning/scoop_bucket](directory/huxiaoning+scoop_bucket.md)** | 📦 70 | ⭐ 1.0 | 🔄 83% |  |

| **[qwerty12/scoop-alts](directory/qwerty12+scoop-alts.md)** | 📦 60 | ⭐ 1.0 | 🔄 78% |  |

| **[li-ruijie/scoop](directory/li-ruijie+scoop.md)** | 📦 59 | ⭐ 1.0 | 🔄 100% |  |

| **[mvrpl/windows-apps](directory/mvrpl+windows-apps.md)** | 📦 53 | ⭐ 1.0 | 🔄 94% |  |

| **[LaelLuo/scoop](directory/LaelLuo+scoop.md)** | 📦 52 | ⭐ 1.0 | 🔄 100% |  |

| **[suquiya/suquiya_bucket](directory/suquiya+suquiya_bucket.md)** | 📦 47 | ⭐ 1.0 | 🔄 96% |  |

| **[apeiraco/scoop-bucket](directory/apeiraco+scoop-bucket.md)** | 📦 46 | ⭐ 1.0 | 🔄 96% |  |

| **[nateify/scoop-nateify](directory/nateify+scoop-nateify.md)** | 📦 46 | ⭐ 1.0 | 🔄 96% |  |

| **[MMKubicki/ScoopBucket](directory/MMKubicki+ScoopBucket.md)** | 📦 43 | ⭐ 1.0 | 🔄 100% |  |

| **[wanstarge/scoopx](directory/wanstarge+scoopx.md)** | 📦 42 | ⭐ 1.0 | 🔄 93% |  |

| **[niceEli/Pail](directory/niceEli+Pail.md)** | 📦 41 | ⭐ 1.0 | 🔄 93% |  |

| **[Spiraster/scoop-bucket](directory/Spiraster+scoop-bucket.md)** | 📦 41 | ⭐ 1.0 | 🔄 93% |  |

| **[Jastmaskerrr/Rojem-Scoop](directory/Jastmaskerrr+Rojem-Scoop.md)** | 📦 41 | ⭐ 1.0 | 🔄 95% |  |

| **[ypxun/scoop_bucket](directory/ypxun+scoop_bucket.md)** | 📦 41 | ⭐ 1.0 | 🔄 100% |  |

| **[kt-devhub/extra](directory/kt-devhub+extra.md)** | 📦 45 | ⭐ 1.0 | 🔄 89% |  |

| **[joaoricarte/jr-bucket](directory/joaoricarte+jr-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 95% |  |

| **[matracey/scoop-bucket](directory/matracey+scoop-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 100% |  |

| **[leic4u/Scoop-Store](directory/leic4u+Scoop-Store.md)** | 📦 38 | ⭐ 1.0 | 🔄 97% |  |

| **[jbwfu/scoop-bucket](directory/jbwfu+scoop-bucket.md)** | 📦 38 | ⭐ 1.0 | 🔄 97% |  |

| **[Lutra-Fs/scoop-bucket](directory/Lutra-Fs+scoop-bucket.md)** | 📦 38 | ⭐ 1.0 | 🔄 95% |  |

| **[NSPC911/le-bucket](directory/NSPC911+le-bucket.md)** | 📦 37 | ⭐ 1.0 | 🔄 97% |  |

| **[Strappazzon/scoop](directory/Strappazzon+scoop.md)** | 📦 36 | ⭐ 1.0 | 🔄 100% |  |

| **[issaclin32/scoop-bucket](directory/issaclin32+scoop-bucket.md)** | 📦 44 | ⭐ 1.0 | 🔄 68% |  |

| **[maoyeedy/Scoop](directory/maoyeedy+Scoop.md)** | 📦 35 | ⭐ 1.0 | 🔄 94% |  |

| **[raisercostin/raiser-scoop-bucket](directory/raisercostin+raiser-scoop-bucket.md)** | 📦 34 | ⭐ 1.0 | 🔄 76% |  |

| **[MagicalDrizzle/scoop-personal](directory/MagicalDrizzle+scoop-personal.md)** | 📦 33 | ⭐ 1.0 | 🔄 79% |  |

| **[janlindblom/scoops](directory/janlindblom+scoops.md)** | 📦 33 | ⭐ 1.0 | 🔄 58% |  |

| **[nicerloop/scoop-nicerloop](directory/nicerloop+scoop-nicerloop.md)** | 📦 32 | ⭐ 1.0 | 🔄 62% |  |

| **[Zevan770/scoop_zev](directory/Zevan770+scoop_zev.md)** | 📦 32 | ⭐ 1.0 | 🔄 91% |  |

| **[ppyv/scoop-jp-fonts](directory/ppyv+scoop-jp-fonts.md)** | 📦 33 | ⭐ 1.0 | 🔄 100% |  |

| **[mslxl/ScoopIt](directory/mslxl+ScoopIt.md)** | 📦 36 | ⭐ 1.0 | 🔄 92% |  |

| **[LucasOe/scoop-lucasoe](directory/LucasOe+scoop-lucasoe.md)** | 📦 33 | ⭐ 1.0 | 🔄 97% |  |

| **[jat001/scoop-ox](directory/jat001+scoop-ox.md)** | 📦 38 | ⭐ 1.0 | 🔄 100% |  |

| **[icecreamZeng/scoop-bucket](directory/icecreamZeng+scoop-bucket.md)** | 📦 29 | ⭐ 1.0 | 🔄 66% |  |

| **[tac091/scoop-multi](directory/tac091+scoop-multi.md)** | 📦 31 | ⭐ 1.0 | 🔄 87% |  |

| **[Bergbok/Scoop-Bucket](directory/Bergbok+Scoop-Bucket.md)** | 📦 28 | ⭐ 1.0 | 🔄 68% |  |

| **[gigberg/localbucket](directory/gigberg+localbucket.md)** | 📦 28 | ⭐ 1.0 | 🔄 75% |  |

| **[amano41/scoop-bucket](directory/amano41+scoop-bucket.md)** | 📦 27 | ⭐ 1.0 | 🔄 96% |  |

| **[rodrigost23/scoop-bucket](directory/rodrigost23+scoop-bucket.md)** | 📦 26 | ⭐ 1.0 | 🔄 96% |  |

| **[pasze888/scoop-keepass](directory/pasze888+scoop-keepass.md)** | 📦 26 | ⭐ 1.0 | 🔄 100% |  |

| **[notPlancha/bucket](directory/notPlancha+bucket.md)** | 📦 29 | ⭐ 1.0 | 🔄 100% |  |

| **[yurical/scoop-mint](directory/yurical+scoop-mint.md)** | 📦 29 | ⭐ 1.0 | 🔄 97% |  |

| **[caoli5288/scoop-bucket](directory/caoli5288+scoop-bucket.md)** | 📦 25 | ⭐ 1.0 | 🔄 84% |  |

| **[cmontage/scoopbucket-soup](directory/cmontage+scoopbucket-soup.md)** | 📦 28 | ⭐ 1.0 | 🔄 100% |  |

| **[Hayxi/Soap](directory/Hayxi+Soap.md)** | 📦 24 | ⭐ 1.0 | 🔄 96% |  |

| **[jonisb/Misc-scoops](directory/jonisb+Misc-scoops.md)** | 📦 23 | ⭐ 1.0 | 🔄 100% |  |

| **[ous50/ous50-bucket](directory/ous50+ous50-bucket.md)** | 📦 23 | ⭐ 1.0 | 🔄 96% |  |

| **[artiga033/Armory](directory/artiga033+Armory.md)** | 📦 22 | ⭐ 1.0 | 🔄 86% |  |

| **[filip2cz/scoop-retro](directory/filip2cz+scoop-retro.md)** | 📦 47 | ⭐ 1.0 | 🔄 2% |  |

| **[strxnge-effects/scoopert](directory/strxnge-effects+scoopert.md)** | 📦 21 | ⭐ 1.0 | 🔄 71% |  |

| **[KO6FCH/scoop-ham](directory/KO6FCH+scoop-ham.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[bodrick/scoop-bucket](directory/bodrick+scoop-bucket.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[crisipa/scoopbucket](directory/crisipa+scoopbucket.md)** | 📦 20 | ⭐ 1.0 | 🔄 100% |  |

| **[Dott-rus/apps](directory/Dott-rus+apps.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[phnthnhnm/Scoop](directory/phnthnhnm+Scoop.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[amorphobia/ScoopMirrored](directory/amorphobia+ScoopMirrored.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[plutotree/scoop-bucket](directory/plutotree+scoop-bucket.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[danalec/scoop-alts](directory/danalec+scoop-alts.md)** | 📦 18 | ⭐ 1.0 | 🔄 89% |  |

| **[ltguillaume/schep](directory/ltguillaume+schep.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[MoonWX/scoop_bucket](directory/MoonWX+scoop_bucket.md)** | 📦 17 | ⭐ 1.0 | 🔄 100% |  |

| **[touhoured/ScoopBucket](directory/touhoured+ScoopBucket.md)** | 📦 17 | ⭐ 1.0 | 🔄 94% |  |

| **[warthurton/scoop-ntwind](directory/warthurton+scoop-ntwind.md)** | 📦 18 | ⭐ 1.0 | 🔄 100% |  |

| **[cainiao1992/scoop-chenxf](directory/cainiao1992+scoop-chenxf.md)** | 📦 17 | ⭐ 1.0 | 🔄 100% |  |

| **[tkit1994/scoop_bucket](directory/tkit1994+scoop_bucket.md)** | 📦 16 | ⭐ 1.0 | 🔄 100% |  |

| **[petlyh/scoop-bucket](directory/petlyh+scoop-bucket.md)** | 📦 16 | ⭐ 1.0 | 🔄 44% |  |

| **[Snowflyt/snowforge](directory/Snowflyt+snowforge.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[bughug/scoop](directory/bughug+scoop.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[prettycation/margin](directory/prettycation+margin.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[nikkoura/scoop-bucket-elitedangerous](directory/nikkoura+scoop-bucket-elitedangerous.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[hmerritt/scoop-bucket](directory/hmerritt+scoop-bucket.md)** | 📦 15 | ⭐ 1.0 | 🔄 93% |  |

| **[kltk/scoop-bucket](directory/kltk+scoop-bucket.md)** | 📦 15 | ⭐ 1.0 | 🔄 100% |  |

| **[haomingz/scoop-bucket](directory/haomingz+scoop-bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 100% |  |

| **[kanami09/Scoop-xPack](directory/kanami09+Scoop-xPack.md)** | 📦 14 | ⭐ 1.0 | 🔄 57% |  |

| **[sbklb1/scoop-bucket](directory/sbklb1+scoop-bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 77% |  |

| **[Edenwize/scoop-apps](directory/Edenwize+scoop-apps.md)** | 📦 13 | ⭐ 1.0 | 🔄 46% |  |

| **[santarl/scoop_bucket](directory/santarl+scoop_bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 86% |  |

| **[ddavness/scoop-roblox](directory/ddavness+scoop-roblox.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[WenSimEHRP/OpenTTD-bucket](directory/WenSimEHRP+OpenTTD-bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[ifvlaboratory/ScoopBucket-ifvlab](directory/ifvlaboratory+ScoopBucket-ifvlab.md)** | 📦 12 | ⭐ 1.0 | 🔄 83% |  |

| **[JotmKKmkLTzE/Scoop-apps](directory/JotmKKmkLTzE+Scoop-apps.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[baaamn/Scoopercalifragilisticexpialidocious](directory/baaamn+Scoopercalifragilisticexpialidocious.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[swxfe/miscbucket](directory/swxfe+miscbucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[Jojo4GH/scoop-JojoIV](directory/Jojo4GH+scoop-JojoIV.md)** | 📦 11 | ⭐ 1.0 | 🔄 91% |  |

| **[jack-mil/scoop-bucket](directory/jack-mil+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[nostorg/scoop-nostr](directory/nostorg+scoop-nostr.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[pierreteam/scoop-js-engine](directory/pierreteam+scoop-js-engine.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[kenjiwho/scoop-bucket](directory/kenjiwho+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[ycrack/scoop-ycrack](directory/ycrack+scoop-ycrack.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[lucaspimentel/scoop-bucket](directory/lucaspimentel+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[warthurton/scoop-misc](directory/warthurton+scoop-misc.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[nonperforming/scoop-godot](directory/nonperforming+scoop-godot.md)** | 📦 12 | ⭐ 1.0 | 🔄 0% |  |

| **[bbkane/scoop-bucket](directory/bbkane+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 0% |  |

| **[insomnimus/scoop-bucket](directory/insomnimus+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 100% |  |

| **[Vodes/Bucket](directory/Vodes+Bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[narnaud/scoop-bucket](directory/narnaud+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[chrismeller/scoop-bucket](directory/chrismeller+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[muxinxy/scoop-bucket](directory/muxinxy+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[MahdiAkrami01/scoop-bucket](directory/MahdiAkrami01+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[haukuen/endless](directory/haukuen+endless.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[Virakal/ScoopBucket](directory/Virakal+ScoopBucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[guitarrapc/scoop-bucket](directory/guitarrapc+scoop-bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[NECOtype/dip](directory/NECOtype+dip.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[pynappo/scoop-bucket](directory/pynappo+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[rsteube/scoop-bucket](directory/rsteube+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[jonz94/scoop-personal](directory/jonz94+scoop-personal.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[henshouse/scoop](directory/henshouse+scoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 88% |  |

| **[Nevuly/frostbite](directory/Nevuly+frostbite.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[urihcim/scoop-urihcim](directory/urihcim+scoop-urihcim.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[fahim-ahmed05/scoop-bucket](directory/fahim-ahmed05+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[AndreiVernon/scoop-cone](directory/AndreiVernon+scoop-cone.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[AureateGarden/Zeo-Apps](directory/AureateGarden+Zeo-Apps.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[RuiNtD/my-scoop-bucket](directory/RuiNtD+my-scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[BinToss/scoop-bucket](directory/BinToss+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[YDX-2147483647/scoop-bucket](directory/YDX-2147483647+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[yi-Xu-0100/scoop-bucket](directory/yi-Xu-0100+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |

| **[dyuu7/docket](directory/dyuu7+docket.md)** | 📦 10 | ⭐ 1.0 | 🔄 80% |  |

| **[zhangchaoza/scoop-extensions-bucket](directory/zhangchaoza+scoop-extensions-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 80% |  |

| **[Bennett-Yang/benckets](directory/Bennett-Yang+benckets.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[kengwang/scoop-bucket-kw](directory/kengwang+scoop-bucket-kw.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[back-lacking/personal-scoop](directory/back-lacking+personal-scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 29% |  |

| **[john180/scoop-bucket](directory/john180+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[bharatvaj/scoop-based](directory/bharatvaj+scoop-based.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[lkhrs/eve-tools](directory/lkhrs+eve-tools.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[stasjok/my-scoop-bucket](directory/stasjok+my-scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[RemySkye/RemyScoop](directory/RemySkye+RemyScoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 43% |  |

| **[felixmaker/scoop-felixmaker](directory/felixmaker+scoop-felixmaker.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[Deskehs/personalBucket](directory/Deskehs+personalBucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[Siphalor/scoop-bucket](directory/Siphalor+scoop-bucket.md)** | 📦 14 | ⭐ 1.0 | 🔄 100% |  |

| **[robinovitch61/scoop-bucket](directory/robinovitch61+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[Exterminate5573/ScoopBucket](directory/Exterminate5573+ScoopBucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[mtpdx/scoop-bucket](directory/mtpdx+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[SwingURM/scoop_bucket](directory/SwingURM+scoop_bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[sammary114/self-custom](directory/sammary114+self-custom.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[qwjyh/scoop_bucket](directory/qwjyh+scoop_bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[BoringBoredom/scoop-bucket](directory/BoringBoredom+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[schmitzCatz/awesome-scoop-bucket](directory/schmitzCatz+awesome-scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/unity3d](directory/tree-s+unity3d.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[zhangfeiran/mybucket](directory/zhangfeiran+mybucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 50% |  |

| **[j1g5awi/scoop-jigsaw](directory/j1g5awi+scoop-jigsaw.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[endowdly/endo-scoop](directory/endowdly+endo-scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 71% |  |

| **[dearrrfish/scoop-bucket](directory/dearrrfish+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[go-feature-flag/scoop](directory/go-feature-flag+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 0% |  |

| **[0x0003/0x0003-s-bucket](directory/0x0003+0x0003-s-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[SnowSquire/scoop](directory/SnowSquire+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[Fleafa/myBucket](directory/Fleafa+myBucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[bgsulz/bgsulz-Bucket](directory/bgsulz+bgsulz-Bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 60% |  |

| **[aliesbelik/astro](directory/aliesbelik+astro.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[pact-foundation/scoop](directory/pact-foundation+scoop.md)** | 📦 7 | ⭐ 1.0 | 🔄 0% |  |

| **[hrshtst/scoop-bucket](directory/hrshtst+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[scowalt/scoop-apps](directory/scowalt+scoop-apps.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[amreus/bucket](directory/amreus+bucket.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[coatl-dev/scoop-coatl-dev](directory/coatl-dev+scoop-coatl-dev.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[gitfool/scoop-vpinball](directory/gitfool+scoop-vpinball.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[loustact/locket](directory/loustact+locket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[mistyrosetta/mistyscoop](directory/mistyrosetta+mistyscoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[goark/scoop-bucket](directory/goark+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[Velgus/Scoop-Velgus](directory/Velgus+Scoop-Velgus.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[arrow2nd/scoop-bucket](directory/arrow2nd+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[emotion3459/Bucket](directory/emotion3459+Bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[NoPlagiarism/noplag](directory/NoPlagiarism+noplag.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[iliqiliev/iliya-bucket](directory/iliqiliev+iliya-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[WyvernIXTL/stupid-bucket](directory/WyvernIXTL+stupid-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[schnow265/scoopet](directory/schnow265+scoopet.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[kaweezle/scoop-bucket](directory/kaweezle+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 0% |  |

| **[quardbreak/scoop-bucket](directory/quardbreak+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[sunfkny/scoop-bucket](directory/sunfkny+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[Dumpinground/expert-eureka](directory/Dumpinground+expert-eureka.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[wtbxsjy/mattress](directory/wtbxsjy+mattress.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[Koalhack/SCrispyBucket](directory/Koalhack+SCrispyBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 71% |  |

| **[zknx/scoop-bucket](directory/zknx+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[DenisionSoft/scoop-box](directory/DenisionSoft+scoop-box.md)** | 📦 5 | ⭐ 1.0 | 🔄 40% |  |

| **[itsHardStyl3r/scoop-personal](directory/itsHardStyl3r+scoop-personal.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[filip2cz/scoop-installers](directory/filip2cz+scoop-installers.md)** | 📦 4 | ⭐ 1.0 | 🔄 50% |  |

| **[Animesh-Ghosh/kulfi-scoop](directory/Animesh-Ghosh+kulfi-scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[Ziyph/Scoop](directory/Ziyph+Scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[mitoteam/scoop-bucket](directory/mitoteam+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[Zalk0/ZalkosBucket](directory/Zalk0+ZalkosBucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[DeltaLaboratory/lemon](directory/DeltaLaboratory+lemon.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[Yukari0201/scoop-bucket](directory/Yukari0201+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[eclecticbouquet/pail](directory/eclecticbouquet+pail.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[qiazo/scoop-bucket](directory/qiazo+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[somaz94/scoop-bucket](directory/somaz94+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[Deaquay/scoop-bucket](directory/Deaquay+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[rfnash/scoop](directory/rfnash+scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[peterrichards-lr/scoop-bucket](directory/peterrichards-lr+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[tech189/tech189-bucket](directory/tech189+tech189-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 100% |  |

| **[JHXs/MyBucket](directory/JHXs+MyBucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[indra87g/awesome-indonesia-dev](directory/indra87g+awesome-indonesia-dev.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[fredjoseph/scoop-bucket](directory/fredjoseph+scoop-bucket.md)** | 📦 8 | ⭐ 1.0 | 🔄 88% |  |

| **[zandercodes/scoop-pangolin](directory/zandercodes+scoop-pangolin.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ShihaoShenDev/ScoopBucket](directory/ShihaoShenDev+ScoopBucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[vladhietala/vlad-scoop-bucket](directory/vladhietala+vlad-scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[jbangdev/scoop-bucket](directory/jbangdev+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[ba230t/scoop-bucket](directory/ba230t+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/arc](directory/tree-s+arc.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/windowsSDK](directory/tree-s+windowsSDK.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[max-sn/personal-bucket](directory/max-sn+personal-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[toddyoe/scoop-canary](directory/toddyoe+scoop-canary.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[t-mart/bucket](directory/t-mart+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[xiongnemo/windows-binaries-scoop-bucket](directory/xiongnemo+windows-binaries-scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[xavidop/scoop-bucket](directory/xavidop+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Hzbeta/scoop-zephyr](directory/Hzbeta+scoop-zephyr.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Nerixyz/silly-bucket](directory/Nerixyz+silly-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[TechPro424/scoop-bucket](directory/TechPro424+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[madLinux7/scoop-bucket](directory/madLinux7+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[70sh1/jug](directory/70sh1+jug.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[gildas/scoop-bucket](directory/gildas+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tbnguyen1407/scoop-bucket](directory/tbnguyen1407+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[FriesI23/scoop-bucket](directory/FriesI23+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[babarot/scoop-bucket](directory/babarot+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[kemokemo/scoop-bucket](directory/kemokemo+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 0% |  |

| **[sbolch/ScoopV](directory/sbolch+ScoopV.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[damienbutt/scoop-bucket](directory/damienbutt+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[nzbr/scoop-bucket](directory/nzbr+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[speratus/redot-engine-bucket](directory/speratus+redot-engine-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[perryhq/perryhq-scoop](directory/perryhq+perryhq-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[cppbear/scoop-cppbear](directory/cppbear+scoop-cppbear.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[amrbashir/scoop-bucket](directory/amrbashir+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ArmoryNode/PersonalScoopBucket](directory/ArmoryNode+PersonalScoopBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[SamTherapy/scoop](directory/SamTherapy+scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[ddanielsantos/dd-bucket](directory/ddanielsantos+dd-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[Mufi-Lang/mufi-bucket](directory/Mufi-Lang+mufi-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[nightshadecf/scoop-bucket](directory/nightshadecf+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[ClaudiaHeart/scoop-bucket-claudiaheart](directory/ClaudiaHeart+scoop-bucket-claudiaheart.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[OmyDaGreat/MaleficBucket](directory/OmyDaGreat+MaleficBucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[auth0/scoop-auth0-cli](directory/auth0+scoop-auth0-cli.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[psmux/scoop-psmux](directory/psmux+scoop-psmux.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[rustfs/scoop-bucket](directory/rustfs+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/virtualbox](directory/tree-s+virtualbox.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[kdash-rs/scoop-kdash](directory/kdash-rs+scoop-kdash.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ipatalas/scoop-bucket](directory/ipatalas+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[kubri/scoop-bucket](directory/kubri+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[mohitmishra786/scoop-bucket](directory/mohitmishra786+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Nimblesite/scoop-bucket](directory/Nimblesite+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[systempromptio/scoop-bucket](directory/systempromptio+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[RTF22/scoop-vocix](directory/RTF22+scoop-vocix.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[monkescience/scoop-bucket](directory/monkescience+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ionos-cloud/scoop-bucket](directory/ionos-cloud+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[AChep/keyguard-repo-scoop](directory/AChep+keyguard-repo-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Gildedter/scoop-bucket](directory/Gildedter+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[BobH-Official/bobh-scoop-bucket](directory/BobH-Official+bobh-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ysthakur/my-scoop-extras](directory/ysthakur+my-scoop-extras.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[prskr/scoop-the-prancing-package](directory/prskr+scoop-the-prancing-package.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[TheRealOwenJ/LimeAndLemon](directory/TheRealOwenJ+LimeAndLemon.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[geekifier/underscoop](directory/geekifier+underscoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[emilio-toledo/scoop-bucket](directory/emilio-toledo+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tokentopapp/scoop-tokentop](directory/tokentopapp+scoop-tokentop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[louiss0/the-code-fixer-23-buckets](directory/louiss0+the-code-fixer-23-buckets.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[debugtheworldbot/scoop-keystats](directory/debugtheworldbot+scoop-keystats.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[macleod-ee/scoop](directory/macleod-ee+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[terraform-docs/scoop-bucket](directory/terraform-docs+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ecsdeployer/scoop-bucket](directory/ecsdeployer+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[henrygd/beszel-scoops](directory/henrygd+beszel-scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[xhorntail/xho-scoops](directory/xhorntail+xho-scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[nareshnavinash/scoop-bucket](directory/nareshnavinash+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[dev-tonholo/scoop-svg-to-compose](directory/dev-tonholo+scoop-svg-to-compose.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[stefanlogue/scoops](directory/stefanlogue+scoops.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[PranavU-Coder/scoop-bucket](directory/PranavU-Coder+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[timrabl/scoop-bucket](directory/timrabl+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[shoehorn-dev/scoop-bucket](directory/shoehorn-dev+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[yazeed/scoop-bucket-proc](directory/yazeed+scoop-bucket-proc.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[voicemeet/scoop-bucket](directory/voicemeet+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[mlm-games/buckets-scoop](directory/mlm-games+buckets-scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[sebastianappelberg/scoop-bucket](directory/sebastianappelberg+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[caffeine-addictt/scoop-bucket](directory/caffeine-addictt+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[mthmulders/scoop-mcs](directory/mthmulders+scoop-mcs.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[danielealbano/scoop-mcp-tools](directory/danielealbano+scoop-mcp-tools.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Gasoid/baker-scoop](directory/Gasoid+baker-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[wsgtcyx/PDF-zusammenfuegen-scoop](directory/wsgtcyx+PDF-zusammenfuegen-scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/GBStudio](directory/tree-s+GBStudio.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[DoveBoy/Scoop-Bucket](directory/DoveBoy+Scoop-Bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[roma-glushko/scoop-tango](directory/roma-glushko+scoop-tango.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[sarub0b0/scoop-bucket](directory/sarub0b0+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[nikkoura/scoop-bucket-vkb](directory/nikkoura+scoop-bucket-vkb.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[WenSimEHRP/wenmisc-bucket](directory/WenSimEHRP+wenmisc-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 20% |  |

| **[sohamw03/Scoop-Bucket](directory/sohamw03+Scoop-Bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[StasysMusial/scoop-bucket](directory/StasysMusial+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[dom1torii/cs2](directory/dom1torii+cs2.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[rafalohaki/oofscoop](directory/rafalohaki+oofscoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Bedingled403/scoop-cool](directory/Bedingled403+scoop-cool.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[004Ongoro/scoop-bucket](directory/004Ongoro+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[leonismoe/scoop-bucket](directory/leonismoe+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[belleradh/birdbucket](directory/belleradh+birdbucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ultimateanu/homebrew-software](directory/ultimateanu+homebrew-software.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[wenmin92/scoop-wenmin92](directory/wenmin92+scoop-wenmin92.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[ypurpl/bucket](directory/ypurpl+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[cmvanb/scoop-bucket](directory/cmvanb+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[sbolch/ScoopZed](directory/sbolch+ScoopZed.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Lelio88/he-bucket](directory/Lelio88+he-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[meenzen/scoop](directory/meenzen+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[yanghanlin/orihime-first](directory/yanghanlin+orihime-first.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[tree-s/mIRC](directory/tree-s+mIRC.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[evg4b/scoop-bucket](directory/evg4b+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aisair/scoop-bucket](directory/aisair+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[ankddev/scoop-ankddev](directory/ankddev+scoop-ankddev.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[nettracex/nettracex-bucket](directory/nettracex+nettracex-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[nginx/scoop-bucket](directory/nginx+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[dh6wk/ScoopRepo](directory/dh6wk+ScoopRepo.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[rayun56/scoop-bucket](directory/rayun56+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[rocketblend/scoop-bucket](directory/rocketblend+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Overimagine1/Poop](directory/Overimagine1+Poop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[jazzwang/scoop-bucket](directory/jazzwang+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[ldez/scoop-bucket](directory/ldez+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[txyyh/Scoop](directory/txyyh+Scoop.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[jahanbani/scoop-anaconda3](directory/jahanbani+scoop-anaconda3.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[SunsetMkt/scoop-aliceincradle](directory/SunsetMkt+scoop-aliceincradle.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[QZLin/winscp-trans](directory/QZLin+winscp-trans.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Absolucy/scoop-lucy](directory/Absolucy+scoop-lucy.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[varabyte/scoop-varabyte](directory/varabyte+scoop-varabyte.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Qile0317/compbio-scoop-bucket](directory/Qile0317+compbio-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Shivelight/scoop-bucket](directory/Shivelight+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[OnlyF0uR/blockchain](directory/OnlyF0uR+blockchain.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Humorist7336/bucket](directory/Humorist7336+bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Der-Floh/scoop-bucket](directory/Der-Floh+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Excalian/scoop](directory/Excalian+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[luke-beep/azrael-scoop](directory/luke-beep+azrael-scoop.md)** | 📦 4 | ⭐ 1.0 | 🔄 0% |  |

| **[KhoiCanDev/scoop-vietnamese-softwares-bucket](directory/KhoiCanDev+scoop-vietnamese-softwares-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 33% |  |

| **[Cooperter/scoop-bucket](directory/Cooperter+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 75% |  |

| **[Bennett-Yang/bencket](directory/Bennett-Yang+bencket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[wind-mask/scoop-bucket-repository](directory/wind-mask+scoop-bucket-repository.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[bacnh85/scoop-bucket](directory/bacnh85+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[jo12bar/scoop-bucket](directory/jo12bar+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Elypha/garden](directory/Elypha+garden.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[Desdaemon/scoop-repo](directory/Desdaemon+scoop-repo.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[lisonge/scoop-ls](directory/lisonge+scoop-ls.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[rnine/scoop-duobolt](directory/rnine+scoop-duobolt.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[wriftai/scoop-bucket](directory/wriftai+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[MichaelHaussmann/scoop-play](directory/MichaelHaussmann+scoop-play.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[tinymce/scoop-bucket](directory/tinymce+scoop-bucket.md)** | 📦 69 | ⭐ 1.0 | 🔄 100% |  |

| **[Orphoros/scoop-bucket](directory/Orphoros+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[skiletro/scoop-vr-software-bucket](directory/skiletro+scoop-vr-software-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[siketyan/scoop-bucket](directory/siketyan+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[h-takesg/h-takesg_bucket](directory/h-takesg+h-takesg_bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[x-idian/scoop-bucket](directory/x-idian+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[DubskySteam/scoop-bucket](directory/DubskySteam+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[kevinboss/maple](directory/kevinboss+maple.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[trdthg/scoop-bucket](directory/trdthg+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[phanirithvij/scop](directory/phanirithvij+scop.md)** | 📦 12 | ⭐ 1.0 | 🔄 75% |  |

| **[SKalt/scoop-git-cc](directory/SKalt+scoop-git-cc.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[ZhenyuXiao/toolbox](directory/ZhenyuXiao+toolbox.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[heroku-miraheze/scoop-bucket](directory/heroku-miraheze+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[SunsetMkt/scoop-vlmcsd](directory/SunsetMkt+scoop-vlmcsd.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/progressquest](directory/tree-s+progressquest.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[rakkateichou/rakbucket](directory/rakkateichou+rakbucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tlipoca9/scoop-bucket](directory/tlipoca9+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[nonperforming/scoop](directory/nonperforming+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aeswibon/scoop-bucket](directory/aeswibon+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[jwt-rs/scoop-jwt-ui](directory/jwt-rs+scoop-jwt-ui.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[upyun/carrot](directory/upyun+carrot.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[elenakrittik/bucket](directory/elenakrittik+bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[darkliquid/bucket](directory/darkliquid+bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Jenway/scoop](directory/Jenway+scoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[negative-authentication/NegativeAuthBucket](directory/negative-authentication+NegativeAuthBucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[onsamyj/dipper](directory/onsamyj+dipper.md)** | 📦 9 | ⭐ 1.0 | 🔄 56% |  |

| **[Daniele-rolli/Beaver-Bucket](directory/Daniele-rolli+Beaver-Bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Dreista/scoop-bucket](directory/Dreista+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[GunMoe/scoop-bucket](directory/GunMoe+scoop-bucket.md)** | 📦 13 | ⭐ 1.0 | 🔄 69% |  |

| **[shrlion/F-one](directory/shrlion+F-one.md)** | 📦 9 | ⭐ 1.0 | 🔄 89% |  |

| **[Dumpinground/openra-mods](directory/Dumpinground+openra-mods.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Dumpinground/emulator-tools](directory/Dumpinground+emulator-tools.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[DelineaXPM/scoop-bucket](directory/DelineaXPM+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Nriver/Scoop-Nriver](directory/Nriver+Scoop-Nriver.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[tree-s/shiftcrypto](directory/tree-s+shiftcrypto.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[aklinovitskiy/scoop-bucket](directory/aklinovitskiy+scoop-bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 50% |  |

| **[syrinka/scoop](directory/syrinka+scoop.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[Sectly/scoop-bucket](directory/Sectly+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[FrostyNick/scoop-bucket](directory/FrostyNick+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[myksmstk/scoop-myks-public](directory/myksmstk+scoop-myks-public.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[Kyure-A/ksb](directory/Kyure-A+ksb.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[herouu/scoop_bucket](directory/herouu+scoop_bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[sirredbeard/determined-bucket](directory/sirredbeard+determined-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[anderlli0053/Staging](directory/anderlli0053+Staging.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[cOborski/chartreuse-triceratops](directory/cOborski+chartreuse-triceratops.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[ncruces/scoop](directory/ncruces+scoop.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[elliot40404/elliot](directory/elliot40404+elliot.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[rexlManu/scoop-bucket](directory/rexlManu+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Notenoughusernames/bluemoon](directory/Notenoughusernames+bluemoon.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[tree-s/fraps](directory/tree-s+fraps.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[acdzh/zpt](directory/acdzh+zpt.md)** | 📦 12 | ⭐ 1.0 | 🔄 100% |  |

| **[skellygore/scoop-bucket](directory/skellygore+scoop-bucket.md)** | 📦 9 | ⭐ 1.0 | 🔄 0% |  |

| **[MANICX100/scoop](directory/MANICX100+scoop.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[foosel/scoop-bucket](directory/foosel+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[burgr033/burgrBucket](directory/burgr033+burgrBucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[subchen/scoop-bucket](directory/subchen+scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[jlaasonen/scoop-bucket](directory/jlaasonen+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Vechro/ryence](directory/Vechro+ryence.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[dem2k/scoop-bucket](directory/dem2k+scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 100% |  |

| **[miketvo/scoop-miketvo](directory/miketvo+scoop-miketvo.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[TronicLabs/troniclabs-buckets](directory/TronicLabs+troniclabs-buckets.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[sebagomez/scoopbucket](directory/sebagomez+scoopbucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[jihuayu/jscoop](directory/jihuayu+jscoop.md)** | 📦 8 | ⭐ 1.0 | 🔄 100% |  |

| **[arcturegulus/scoop](directory/arcturegulus+scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Madh93/scoop-bucket](directory/Madh93+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[gaojr/MyScoopBucket](directory/gaojr+MyScoopBucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Alveel/scoop-bucket](directory/Alveel+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[sveltinio/scoop-sveltin](directory/sveltinio+scoop-sveltin.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[wiuri/wr_scoop_bucket](directory/wiuri+wr_scoop_bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Shemnei/scoop-bucket](directory/Shemnei+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[celsiusnarhwal/kirigiri](directory/celsiusnarhwal+kirigiri.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Skyppex/sky-bucket](directory/Skyppex+sky-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[edavidaja/scoop-bucket](directory/edavidaja+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[tejasraman/Konsole-Scoop](directory/tejasraman+Konsole-Scoop.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[thesilvercraft/SilverCraftBucket](directory/thesilvercraft+SilverCraftBucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[ereborstudios/scoop-bucket](directory/ereborstudios+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[hjjhjj/doraemon-bucket](directory/hjjhjj+doraemon-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[Aldebaranoro/scoop-bucket](directory/Aldebaranoro+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[comp500/scoop-comp500](directory/comp500+scoop-comp500.md)** | 📦 7 | ⭐ 1.0 | 🔄 86% |  |

| **[Logiase/scoop-embedded](directory/Logiase+scoop-embedded.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[pvarentsov/scoop-iola](directory/pvarentsov+scoop-iola.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[littleli/scoop-garage](directory/littleli+scoop-garage.md)** | 📦 31 | ⭐ 1.0 | 🔄 77% |  |

| **[Jeddunk/scoop-bucket](directory/Jeddunk+scoop-bucket.md)** | 📦 10 | ⭐ 1.0 | 🔄 90% |  |

| **[rkolka/scoop-manifold](directory/rkolka+scoop-manifold.md)** | 📦 9 | ⭐ 1.0 | 🔄 56% |  |

| **[pgollangi/scoop-bucket](directory/pgollangi+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[gfieldGG/bucket](directory/gfieldGG+bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[flvinny/scoop-bucket](directory/flvinny+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[JManch/scoop-bucket](directory/JManch+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[xfournet/scoop-sboot](directory/xfournet+scoop-sboot.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[tkishiro/ScoopBucket](directory/tkishiro+ScoopBucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[adamrodger/scoop-bucket](directory/adamrodger+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[backd-io/scoop-bucket](directory/backd-io+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Dumpinground/themes](directory/Dumpinground+themes.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[uxiew/scoop-fruit](directory/uxiew+scoop-fruit.md)** | 📦 7 | ⭐ 1.0 | 🔄 57% |  |

| **[EscWasTaken/scoop-special](directory/EscWasTaken+scoop-special.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[Saw-mon-and-Natalie/scoop-crypto](directory/Saw-mon-and-Natalie+scoop-crypto.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[arnos-stuff/arnos-scoop-bucket](directory/arnos-stuff+arnos-scoop-bucket.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |

| **[TonyZYT2000/scoop-Andromeda](directory/TonyZYT2000+scoop-Andromeda.md)** | 📦 6 | ⭐ 1.0 | 🔄 83% |  |

| **[pasoevi/more-scoops](directory/pasoevi+more-scoops.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[studoot/my-scoop-bucket](directory/studoot+my-scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[zhangfeiran/my-bucket](directory/zhangfeiran+my-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[daekma/scoop-bucket](directory/daekma+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[mvietri/scoop-hela](directory/mvietri+scoop-hela.md)** | 📦 3 | ⭐ 1.0 | 🔄 33% |  |

| **[nimzo6689/Scoop-nimzo6689](directory/nimzo6689+Scoop-nimzo6689.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[Duckle29/duckles_bucket](directory/Duckle29+duckles_bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[fioepq9/scoop-aqua](directory/fioepq9+scoop-aqua.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[cidertool/scoop-bucket](directory/cidertool+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[gpailler/scoop-apps](directory/gpailler+scoop-apps.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[vsviridov/scoop-bucket](directory/vsviridov+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[sambeckingham/dhall](directory/sambeckingham+dhall.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Kazanami/zeus-bucket](directory/Kazanami+zeus-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 60% |  |

| **[CALMorACT/hola_bucket](directory/CALMorACT+hola_bucket.md)** | 📦 18 | ⭐ 1.0 | 🔄 83% |  |

| **[tclog/scoop-tclog](directory/tclog+scoop-tclog.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[GreatGodApollo/trough](directory/GreatGodApollo+trough.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Dumpinground/simulator-tools](directory/Dumpinground+simulator-tools.md)** | 📦 5 | ⭐ 1.0 | 🔄 80% |  |

| **[fire/scoop-fire](directory/fire+scoop-fire.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[AndreasBrostrom/arma3-scoop-bucket](directory/AndreasBrostrom+arma3-scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[jku1995/Jbucket](directory/jku1995+Jbucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 100% |  |

| **[s-oram/bento](directory/s-oram+bento.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[brad-jones/scoop-bucket](directory/brad-jones+scoop-bucket.md)** | 📦 5 | ⭐ 1.0 | 🔄 0% |  |

| **[pigsflew/scoop-arbitrariae](directory/pigsflew+scoop-arbitrariae.md)** | 📦 5 | ⭐ 1.0 | 🔄 100% |  |

| **[garyng/scoop-garyng](directory/garyng+scoop-garyng.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[roose/scoop-tools](directory/roose+scoop-tools.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[prantlf/scoop-bucket](directory/prantlf+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 0% |  |

| **[devcsrj/scoop-bucket](directory/devcsrj+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[Etsinshao/scoop-bucket](directory/Etsinshao+scoop-bucket.md)** | 📦 7 | ⭐ 1.0 | 🔄 100% |  |

| **[colkey/scoop-colkey](directory/colkey+scoop-colkey.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[PorridgePi/scoop-bucket](directory/PorridgePi+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 100% |  |

| **[filippobuletto/pot-pourri](directory/filippobuletto+pot-pourri.md)** | 📦 7 | ⭐ 1.0 | 🔄 57% |  |

| **[leonidboykov/scoop-bucket](directory/leonidboykov+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 0% |  |

| **[Master-Hash/bucket](directory/Master-Hash+bucket.md)** | 📦 4 | ⭐ 1.0 | 🔄 100% |  |

| **[yukihane/scoop-bucket-yukihane](directory/yukihane+scoop-bucket-yukihane.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[aenthill/scoop-bucket](directory/aenthill+scoop-bucket.md)** | 📦 1 | ⭐ 1.0 | 🔄 0% |  |

| **[icedream/scoop-bucket](directory/icedream+scoop-bucket.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[FDUZS/spoon](directory/FDUZS+spoon.md)** | 📦 42 | ⭐ 1.0 | 🔄 98% |  |

| **[TheAsuro/scoop-stuff](directory/TheAsuro+scoop-stuff.md)** | 📦 2 | ⭐ 1.0 | 🔄 100% |  |

| **[Kantouzin/scoop-bucketouzin](directory/Kantouzin+scoop-bucketouzin.md)** | 📦 2 | ⭐ 1.0 | 🔄 50% |  |

| **[nickbudi/scoop-bucket](directory/nickbudi+scoop-bucket.md)** | 📦 30 | ⭐ 1.0 | 🔄 80% |  |

| **[earnestma/scoop-earne](directory/earnestma+scoop-earne.md)** | 📦 10 | ⭐ 1.0 | 🔄 70% |  |

| **[Br1ght0ne/scoop-bucket](directory/Br1ght0ne+scoop-bucket.md)** | 📦 19 | ⭐ 1.0 | 🔄 100% |  |

| **[mogeko/scoop-bucket](directory/mogeko+scoop-bucket.md)** | 📦 11 | ⭐ 1.0 | 🔄 100% |  |

| **[Mushus/scoop-bucket](directory/Mushus+scoop-bucket.md)** | 📦 3 | ⭐ 1.0 | 🔄 67% |  |

| **[tobyvin/scoop-tobyvin](directory/tobyvin+scoop-tobyvin.md)** | 📦 25 | ⭐ 1.0 | 🔄 72% |  |

| **[Harakku/harakkus-scoop-bucket](directory/Harakku+harakkus-scoop-bucket.md)** | 📦 21 | ⭐ 1.0 | 🔄 86% |  |

| **[ProfElements/EmulatorBucket](directory/ProfElements+EmulatorBucket.md)** | 📦 27 | ⭐ 1.0 | 🔄 0% |  |

| **[zt-luo/bucket-luo](directory/zt-luo+bucket-luo.md)** | 📦 6 | ⭐ 1.0 | 🔄 0% |  |


</details>

# 🛠️ Operational Health (Crawler Metrics)
* **Total Crawler Runs**: 17
* **Total Repo Updates**: 661
* **Ecosystem Growth (Since Last Run)**:
  * 🪣 +57 Buckets
  * 📦 +447 Recipes
* **Eviction Count**: 🗑️ 0
* **API Rate Limit Retries**: ⏳ 0
* **Cache Size**: 💾 0.68 MB
* **Pipeline Times (Last Run)**:
  * 🔍 Discovery: 2.68s
  * 📥 Update: 18.64s
* **Cumulative Compute Time**: 8.4 minutes
