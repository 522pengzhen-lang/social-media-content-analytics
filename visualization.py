import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/posts.csv")

df["engagement_score"] = df["likes"] + 2 * df["comments"]

# topic analysis
topic_perf = df.groupby("topic")["engagement_score"].mean()

plt.figure()
topic_perf.plot(kind="bar")
plt.title("Engagement Score by Topic")
plt.ylabel("Engagement Score")
plt.xlabel("Topic")
plt.savefig("charts/topic_engagement.png")
plt.close()


# platform analysis
platform_perf = df.groupby("platform")["engagement_score"].mean()

plt.figure()
platform_perf.plot(kind="bar")
plt.title("Engagement Score by Platform")
plt.ylabel("Engagement Score")
plt.xlabel("Platform")
plt.savefig("charts/platform_engagement.png")
plt.close()


# posting time analysis
time_perf = df.groupby("time")["engagement_score"].mean()

plt.figure()
time_perf.plot(kind="bar")
plt.title("Engagement Score by Posting Time")
plt.ylabel("Engagement Score")
plt.xlabel("Hour")
plt.savefig("charts/time_engagement.png")
plt.close()
