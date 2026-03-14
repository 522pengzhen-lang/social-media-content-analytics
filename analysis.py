import pandas as pd

df = pd.read_csv("data/posts.csv")

# Define a simple engagement score
df["engagement_score"] = df["likes"] + 2 * df["comments"]

print("=== Overall Average Engagement Score ===")
print(df["engagement_score"].mean())

print("\n=== Engagement by Topic ===")
print(df.groupby("topic")["engagement_score"].mean().sort_values(ascending=False))

print("\n=== Engagement by Platform ===")
print(df.groupby("platform")["engagement_score"].mean().sort_values(ascending=False))

print("\n=== Engagement by Posting Time ===")
print(df.groupby("time")["engagement_score"].mean().sort_values(ascending=False))
