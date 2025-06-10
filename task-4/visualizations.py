import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Create visuals directory if it doesn't exist
os.makedirs("./visuals", exist_ok=True)

# Load your processed dataset
df = pd.read_csv('./data/sentiment_results.csv')  # Adjust path if needed

# --------- 1. Sentiment Distribution per Bank ---------
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='bank', hue='sentiment_label', palette='Set2')
plt.title("Sentiment Distribution per Bank")
plt.ylabel("Review Count")
plt.xlabel("Bank")
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('./visuals/sentiment_distribution.png')
plt.close()

# --------- 2. Rating Distribution per Bank ---------
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='rating', hue='bank', palette='Set3')
plt.title("Rating Distribution by Bank")
plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.legend(title="Bank")
plt.tight_layout()
plt.savefig('./visuals/rating_distribution.png')
plt.close()

# --------- 3. Top Keywords per Bank ---------
keywords_df = pd.read_csv('./data/top_keywords_by_bank.csv')  # assumes you created this earlier

for bank in keywords_df['bank'].unique():
    plt.figure(figsize=(10,6))
    subset = keywords_df[keywords_df['bank'] == bank].head(10)
    sns.barplot(data=subset, y='keyword', x='tfidf_score', palette='viridis')
    plt.title(f"Top Keywords for {bank}")
    plt.xlabel("TF-IDF Score")
    plt.ylabel("Keyword")
    plt.tight_layout()
    plt.savefig(f'./visuals/top_keywords_{bank.lower()}.png')
    plt.close()

# --------- 4. Word Clouds per Bank ---------
for bank in df['bank'].unique():
    text = " ".join(df[df['bank'] == bank]['cleaned_review'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Dark2').generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {bank}")
    plt.tight_layout()
    plt.savefig(f'./visuals/wordcloud_{bank.lower()}.png')
    plt.close()

# --------- 5. Sentiment vs Rating ---------
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='rating', y='sentiment_score', hue='bank', palette='pastel')
plt.title("Sentiment Score vs Rating by Bank")
plt.xlabel("Rating")
plt.ylabel("Sentiment Score")
plt.legend(title="Bank")
plt.tight_layout()
plt.savefig('./visuals/sentiment_vs_rating.png')
plt.close()

print("✅ All plots saved in './visuals/' folder.")
