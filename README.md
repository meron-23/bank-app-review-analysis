# Bank App Review Analysis

## Overview
Scraping and preprocessing reviews from Google Play for three major Ethiopian banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Tools
- Python
- google-play-scraper
- pandas

## Methodology

1. **Scraping**: Collected 400+ reviews per bank using `google-play-scraper`.
2. **Cleaning**:
   - Removed duplicates
   - Handled missing values
   - Normalized date format (YYYY-MM-DD)
3. **Output**:
   - `clean_reviews.csv` with columns:
     - `review`, `rating`, `date`, `bank`, `source`

## Repo Structure
```python
bank-app-review-analysis/
│
├── scraper.py
├── preprocess.py
├── raw_reviews.csv
├── clean_reviews.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Progress
- [x] Scrape 1200+ reviews
- [x] Clean & preprocess
- [x] Push meaningful commits on `task-1` branch
