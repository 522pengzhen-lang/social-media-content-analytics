import pandas as pd
from collections import Counter
import re

df = pd.read_csv("data/posts.csv")
df = df.dropna()

df["engagement_score"] = df["likes"] + 2 * df["comments"]

average_score = df["engagement_score"].mean()
high_posts = df[df["engagement_score"] > average_score]

words = []

for title in high_posts["title"]:
    tokens = re.findall(r"[a-zA-Z]+", title.lower())
    words.extend(tokens)

common_words = Counter(words)

print("=== Top Keywords in High-Performing Posts ===")
for word, count in common_words.most_common(10):
    print(f"{word}: {count}")
