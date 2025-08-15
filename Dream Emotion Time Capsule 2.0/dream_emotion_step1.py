# -*- coding: utf-8 -*-
# Step 1: Imports & Setup
import os
import pandas as pd
import numpy as np
from faker import Faker

# Create data folder
os.makedirs("data", exist_ok=True)

# Seed for reproducibility
Faker.seed(42)
np.random.seed(42)

# Step 1: Generate synthetic dream dataset
print("Step 1: Generating synthetic dream dataset...")

fake = Faker()
dreams = []

# Generate 1 year of daily dreams
for i in range(365):
    dream_text = fake.sentence(nb_words=np.random.randint(5, 15))
    dream_date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=i)
    dreams.append({
        "date": dream_date,
        "dream_text": dream_text
    })

df_dreams = pd.DataFrame(dreams)
df_dreams.to_csv("data/dream_journal.csv", index=False)

print("Synthetic dream dataset saved: data/dream_journal.csv ✅")
