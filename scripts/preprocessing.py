import pandas as pd

df = pd.read_csv("./data/raw_reviews.csv")

# Drop duplicates
df = df.drop_duplicates(subset=["review", "date", "bank"])

# Drop rows with missing values
df = df.dropna()

# Ensure date is formatted properly
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save clean data
df.to_csv("./data/clean_reviews.csv", index=False)
