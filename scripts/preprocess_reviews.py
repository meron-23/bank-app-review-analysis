import pandas as pd
import re
import emoji

# Load raw reviews
df = pd.read_csv('./data/raw_reviews.csv')
print(f"Starting with {len(df)} reviews.")

# Remove emojis
def remove_emojis(text):
    return emoji.replace_emoji(str(text), replace='')

df['review'] = df['review'].apply(remove_emojis)

# Remove reviews with Amharic script (Ge'ez)
def contains_amharic(text):
    return bool(re.search(r'[\u1200-\u137F]', str(text)))

df = df[~df['review'].apply(contains_amharic)]

# Remove reviews with transliterated Amharic (Amharic typed in English)
amharic_keywords = ['betam', 'tiru', 'neber', 'yetemeta', 'Masha', 'alla', 'ante', 'dedeb']

def has_transliterated_amharic(text):
    text = str(text).lower()
    return any(word in text for word in amharic_keywords)

df = df[~df['review'].apply(has_transliterated_amharic)]

# Remove reviews that look like names (1-3 capitalized words)
def looks_like_name(text):
    words = str(text).strip().split()
    return 1 <= len(words) <= 3 and all(word.istitle() for word in words)

df = df[~df['review'].apply(looks_like_name)]


# Remove extra spaces & empty reviews
df['review'] = df['review'].str.strip()
df = df[df['review'].str.len() > 0]

# Save cleaned dataset
df.to_csv('./data/cleaned_reviews.csv', index=False)
print(f"Done! You now have {len(df)} clean reviews saved in 'clean_reviews.csv'.")
