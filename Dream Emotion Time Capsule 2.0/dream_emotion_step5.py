# Step 5: Wordcloud & Insights
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/dream_journal_emotion.csv")

# Combine all dream texts
all_text = " ".join(df['dream_text'].tolist())

# Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(all_text)

# Plot WordCloud
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Most Common Words in Dreams", fontsize=20)
plt.show()

# Simple Insights
emotion_counts = df['emotion'].value_counts()
print("\nDream Emotion Distribution:\n")
print(emotion_counts)

most_common_words = pd.Series(" ".join(df['dream_text']).lower().split()).value_counts().head(10)
print("\nTop 10 most common words in dreams:\n")
print(most_common_words)

print("\nWordcloud & insights generation completed ✅")
