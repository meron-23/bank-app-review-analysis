import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_sm")
df = pd.read_csv("./data/cleaned_reviews.csv")

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

df["cleaned_review"] = df["review"].astype(str).apply(clean_text)
df.to_csv("./data/preprocessed_reviews.csv", index=False)
