from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("./data/preprocessed_reviews.csv")

tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=2, stop_words='english')

# Collect rows for the final CSV
keyword_rows = []

for bank in df['bank'].unique():
    bank_reviews = df[df['bank'] == bank]['cleaned_review'].dropna()
    tfidf_matrix = tfidf.fit_transform(bank_reviews)
    scores = zip(tfidf.get_feature_names_out(), tfidf_matrix.sum(axis=0).A1)
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    top_keywords = sorted_keywords[:20]

    # Append to the list with bank name and keyword
    for keyword, score in top_keywords:
        keyword_rows.append({
            'bank': bank,
            'keyword': keyword,
            'tfidf_score': round(score, 4)
        })

# Create DataFrame and save to CSV
keywords_df = pd.DataFrame(keyword_rows)
keywords_df.to_csv("./data/top_keywords_per_bank.csv", index=False)

print("✅ Top keywords per bank saved to ./data/top_keywords_per_bank.csv")


