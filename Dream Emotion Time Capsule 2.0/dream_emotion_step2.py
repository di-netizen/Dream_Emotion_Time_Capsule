# Step 2: Emotion Detection
import pandas as pd
import numpy as np

# Load synthetic dream dataset
df_dreams = pd.read_csv("data/dream_journal.csv")

# Define emotion keywords
happy_words = ["happy", "joy", "fun", "smile", "laugh", "play", "celebrate"]
sad_words = ["sad", "cry", "lonely", "loss", "tear", "pain"]
anxious_words = ["afraid", "scared", "dark", "lost", "fear", "worry"]

# Function to assign emotion based on dream text
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in happy_words):
        return "happy"
    elif any(word in text for word in sad_words):
        return "sad"
    elif any(word in text for word in anxious_words):
        return "anxious"
    else:
        # Random assignment if no keywords found
        return np.random.choice(["happy", "sad", "anxious", "neutral"])

# Apply function to all dreams
df_dreams["emotion"] = df_dreams["dream_text"].apply(detect_emotion)

# Save updated dataset
df_dreams.to_csv("data/dream_journal_emotion.csv", index=False)
print("Emotion assigned dataset saved: data/dream_journal_emotion.csv ✅")
