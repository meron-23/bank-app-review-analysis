from google_play_scraper import reviews
import pandas as pd

bank_apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in bank_apps.items():
    print(f"Scraping {bank}...")
    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        count=400,
        filter_score_with=None
    )
    print(f"{bank}: {len(result)} reviews scraped.")
    for entry in result:
        all_reviews.append({
            "review": entry['content'],
            "rating": entry['score'],
            "date": entry['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
print(df.head)
df.to_csv("raw_reviews.csv", index=False)
