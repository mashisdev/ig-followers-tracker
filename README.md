# 📷Instagram Follower Analyzer

A simple Python script to analyze your Instagram followers and following data exported from your account. It classifies users into three categories:

- ✅ **Mutual Followers** – people you follow and who follow you back.
- 👀 **Followers only** – people who follow you, but you don't follow them back.
- 👉 **Following only** – people you follow, but who don’t follow you back.

## 📁Input Files

This script expects two JSON files:

- `followers_1.json`: Your followers list, with the structure exported by Instagram.
- `following.json`: Your following list, also exported by Instagram.

Make sure to keep the original structure from Instagram's data download. Example folder structure:
```bash
project/
├── followers_1.json
├── following.json
├── analyze_followers.py
└── README.md
```

## ▶️How to Use

1. Export your Instagram data from the **Meta Accounts Center** (https://accountscenter.meta.com/info_and_permissions).
2. Download and unzip the data.
3. Place the `followers_1.json` and `following.json` files in the same directory as the script.
4. Run the script:

```bash
python analyze_followers.py
