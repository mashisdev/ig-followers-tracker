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

1. Open Instagram in a web browser and log in to your account.  
2. Go to your profile and click ⚙️ **Settings** (or tap the three lines menu > **Your activity** > **Download your information**).  
3. **Download or transfer information**

   ![image](https://github.com/user-attachments/assets/f13a01a6-5d01-4c2d-b52a-02103f545ddb)

4. Select your Instagram account ✅

   ![image](https://github.com/user-attachments/assets/54c9a6fc-528f-4abb-a4ae-0adc114c6af9)

5. **Some of your information**

   ![image](https://github.com/user-attachments/assets/a41d6cbf-cb1c-4e0d-bb08-0b272bf1ce81)

6. Followers and following ✅

   ![image](https://github.com/user-attachments/assets/80bdd26e-03b1-45ae-8fd3-222c4cf8c768)
   
7. **Download to device**

   ![image](https://github.com/user-attachments/assets/54362d28-af93-4ba6-90d6-b658224a70d0)
   
8. Choose **JSON** format and **All time** date range

   ![image](https://github.com/user-attachments/assets/5e746b9e-4cd0-4a19-99e3-b1c41f0eb365)

9. Instagram will email you a ZIP download link

   ![image](https://github.com/user-attachments/assets/a335b885-b5e5-451d-8275-3eb4b22f7494)
   
10. Extract it and locate the files `followers_1.json` and `following.json`. They are usually located in the `followers_and_following/` folder

    ![image](https://github.com/user-attachments/assets/057d8ba1-a302-428a-8c17-d700c4dddf2e)

11. Place the `followers_1.json` and `following.json` files in the same directory as the script.
12. Run the script: `python analyze_followers.py`
