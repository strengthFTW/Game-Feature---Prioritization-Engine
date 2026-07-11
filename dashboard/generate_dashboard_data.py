import pandas as pd
import json
import numpy as np

BASE = "../data/processed"

# 1. Priority report
priority_df = pd.read_csv(f"{BASE}/feature_priority_report.csv")

# 2. Keywords
with open(f"{BASE}/top_keywords.json") as f:
    keywords = json.load(f)

# 3. Timeline
df_raw = pd.read_csv(f"{BASE}/cleaned_reviews.csv", usecols=["created", "voted_up"])
df_raw["created"] = pd.to_datetime(df_raw["created"], unit="s", errors="coerce")
df_raw = df_raw.dropna(subset=["created"])
df_raw["month"] = df_raw["created"].dt.to_period("M").astype(str)
timeline = (
    df_raw.groupby("month")
    .agg(total=("voted_up", "count"), positive=("voted_up", "sum"))
    .reset_index()
)
timeline["negative"] = timeline["total"] - timeline["positive"]
timeline = timeline[timeline["month"] >= "2020-01"].tail(40)

# 4. Sentiment by feature
sentiment_df = pd.read_csv(f"{BASE}/sentiment_by_feature.csv")

# 5. Assemble dashboard data
data = {
    "meta": {
        "game": "Cyberpunk 2077",
        "total_reviews": int(df_raw["voted_up"].count()),
        "total_positive": int(df_raw["voted_up"].sum()),
        "total_negative": int((df_raw["voted_up"] == False).sum()),
        "features_analyzed": int(len(priority_df)),
        "overall_positive_rate": round(df_raw["voted_up"].mean() * 100, 1),
    },
    "priority_report": priority_df.to_dict(orient="records"),
    "sentiment_by_feature": sentiment_df.to_dict(orient="records"),
    "keywords": keywords,
    "timeline": timeline.to_dict(orient="records"),
}

output_path = "data.json"
with open(output_path, "w") as f:
    json.dump(data, f, indent=2, default=str)

print(f"Dashboard data saved to {output_path}")
print(f"  Total reviews: {data['meta']['total_reviews']:,}")
print(f"  Positive rate: {data['meta']['overall_positive_rate']}%")
print(f"  Features analyzed: {data['meta']['features_analyzed']}")
print(f"  Timeline months: {len(data['timeline'])}")
