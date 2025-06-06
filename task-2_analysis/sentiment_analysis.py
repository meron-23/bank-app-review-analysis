from transformers import pipeline
import pandas as pd

df = pd.read_csv("./data/preprocessed_reviews.csv")

sent_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    try:
        result = sent_pipeline(text[:512])[0]
        return pd.Series([result['label'], result['score']])
    except:
        return pd.Series([None, None])

df[["sentiment_label", "sentiment_score"]] = df["cleaned_review"].apply(get_sentiment)
df.to_csv("./data/sentiment_results.csv", index=False)
