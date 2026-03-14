import pandas as pd
from collections import Counter
import re

df = pd.read_csv("data/posts.csv")
df = df.dropna()

df["engagement_score"] = df["likes"] + 2 * df["comments"]

best_topic = df.groupby("topic")["engagement_score"].mean().idxmax()
best_time = df.groupby("time")["engagement_score"].mean().idxmax()
best_platform = df.groupby("platform")["engagement_score"].mean().idxmax()

average_score = df["engagement_score"].mean()
high_posts = df[df["engagement_score"] > average_score]

words = []
for title in high_posts["title"]:
    tokens = re.findall(r"[a-zA-Z]+", title.lower())
    words.extend(tokens)

common_words = Counter(words)
top_keywords = [word for word, count in common_words.most_common(3)]

print("=== Content Recommendation ===")
print(f"Recommended topic: {best_topic}")
print(f"Best posting time: {best_time}:00")
print(f"Best-performing platform: {best_platform}")
print(f"Suggested keywords: {', '.join(top_keywords)}")
