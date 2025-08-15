# Step 3: Timeline Analysis & Visualization
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with emotions
df = pd.read_csv("data/dream_journal_emotion.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Aggregate emotions by week
df['week'] = df['date'].dt.isocalendar().week
weekly_emotions = df.groupby(['week', 'emotion']).size().unstack(fill_value=0)

# Plot weekly emotion trends
plt.figure(figsize=(12,6))
for emotion in weekly_emotions.columns:
    plt.plot(weekly_emotions.index, weekly_emotions[emotion], label=emotion.capitalize())

plt.xlabel("Week Number")
plt.ylabel("Number of Dreams")
plt.title("Weekly Dream Emotion Trends")
plt.legend()
plt.grid(True)
plt.show()

# Optional: monthly aggregation
df['month'] = df['date'].dt.month
monthly_emotions = df.groupby(['month', 'emotion']).size().unstack(fill_value=0)
monthly_emotions.plot(kind='bar', stacked=True, figsize=(12,6))
plt.title("Monthly Dream Emotion Distribution")
plt.xlabel("Month")
plt.ylabel("Number of Dreams")
plt.show()

print("Timeline analysis & visualization completed ✅")
