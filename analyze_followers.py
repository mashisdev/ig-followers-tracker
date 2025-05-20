import json

with open("followers_1.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open("following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)["relationships_following"]

followers_usernames = {entry["string_list_data"][0]["value"] for entry in followers_data}
following_usernames = {entry["string_list_data"][0]["value"] for entry in following_data}

mutual_followers = followers_usernames & following_usernames
only_followers = followers_usernames - following_usernames
only_following = following_usernames - followers_usernames

print("✅ Mutual Followers (you follow each other):")
print(sorted(mutual_followers))

print("\n👀 Followers only (they follow you):")
print(sorted(only_followers))

print("\n👉 Following only (you follow them):")
print(sorted(only_following))

result = {
    "mutual_followers": list(mutual_followers),
    "only_followers": list(only_followers),
    "only_following": list(only_following)
}
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)