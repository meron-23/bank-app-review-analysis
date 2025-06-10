import cx_Oracle
import pandas as pd

# Load your data
df = pd.read_csv("./data/cleaned_reviews.csv")

# Connect to Oracle
dsn_tns = cx_Oracle.makedsn('192.168.1.3', 1521, service_name='XE') 
conn = cx_Oracle.connect(user='system', password='meronyeyenekonjo24', dsn=dsn_tns)
cursor = conn.cursor()

# Insert unique banks
bank_ids = {}
for bank in df['bank'].dropna().unique():
    cursor.execute("""
        MERGE INTO banks b USING (SELECT :1 AS name FROM dual) d
        ON (b.name = d.name)
        WHEN NOT MATCHED THEN INSERT (name) VALUES (:1)
    """, [bank])
    cursor.execute("SELECT id FROM banks WHERE name = :1", [bank])
    bank_ids[bank] = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    bank_id = bank_ids.get(row['bank'])
    rating = row['rating'] if not pd.isna(row['rating']) else None
    review = row['review']
    source = row['source'] if not pd.isna(row['source']) else "Unknown"
    review_date = row['date'] if not pd.isna(row['date']) else "2025-06-01"

    cursor.execute("""
        INSERT INTO reviews (bank_id, review, rating, review_date, source)
        VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)
    """, (bank_id, review, rating, review_date, source))

# Commit and close
conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully.")


