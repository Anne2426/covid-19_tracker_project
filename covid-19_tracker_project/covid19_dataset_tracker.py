
# covid19_dataset_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("covid19_data.csv", parse_dates=["Date"])
print("🔍 Dataset Preview:")
print(df.head())

# Summary: Latest data for each country
latest_data = df[df["Date"] == df["Date"].max()]
top10 = latest_data.sort_values(by="Confirmed", ascending=False).head(10)

# Plot: Top 10 countries by total confirmed cases
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Country", y="Confirmed", palette="Reds_r")
plt.title("Top 10 Countries by Confirmed COVID-19 Cases (Latest Date)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_covid_countries_dataset.png")
plt.show()

# Trend: India COVID-19 progression over time
india = df[df["Country"] == "INDIA"]

plt.figure(figsize=(10, 5))
plt.plot(india["Date"], india["Confirmed"], marker='o', label="Confirmed")
plt.plot(india["Date"], india["Recovered"], marker='s', label="Recovered")
plt.plot(india["Date"], india["Deaths"], marker='^', label="Deaths")
plt.title("COVID-19 Trend in India")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("india_covid_trend.png")
plt.show()
