# Step 4: Predict Future Emotional Trends
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/dream_journal_emotion.csv")
df['date'] = pd.to_datetime(df['date'])

# Aggregate weekly emotion counts
df['week'] = df['date'].dt.isocalendar().week
weekly_emotions = df.groupby(['week', 'emotion']).size().unstack(fill_value=0)

# Prepare prediction model for each emotion
future_weeks = np.arange(weekly_emotions.index.max()+1, weekly_emotions.index.max()+5).reshape(-1,1)  # next 4 weeks

predictions = {}

for emotion in weekly_emotions.columns:
    X = weekly_emotions.index.values.reshape(-1,1)
    y = weekly_emotions[emotion].values
    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict(future_weeks)
    predictions[emotion] = np.round(pred).astype(int)

# Display predictions
pred_df = pd.DataFrame(predictions, index=future_weeks.flatten())
print("\nPredicted emotion counts for next 4 weeks:\n")
print(pred_df)

# Visualization
plt.figure(figsize=(12,6))
for emotion in weekly_emotions.columns:
    plt.plot(list(weekly_emotions.index) + list(future_weeks.flatten()),
             list(weekly_emotions[emotion]) + list(predictions[emotion]),
             label=f"{emotion.capitalize()} (including forecast)", marker='o')

plt.xlabel("Week Number")
plt.ylabel("Number of Dreams")
plt.title("Dream Emotion Trends with Forecast")
plt.legend()
plt.grid(True)
plt.show()

print("\nFuture emotion prediction completed ✅")
