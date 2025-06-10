-- generate_dump.sql
SET HEADING OFF
SET FEEDBACK OFF
SET PAGESIZE 0
SET LINESIZE 1000
SET LONG 5000
SET TRIMSPOOL ON
SET TERMOUT OFF
SET ECHO OFF

SPOOL bank_reviews_dump.sql

-- Dump banks table
SELECT 'INSERT INTO banks (id, name) VALUES (' || id || ', ''' || REPLACE(name, '''', '''''') || ''');'
FROM banks;

-- Dump reviews table
SELECT 'INSERT INTO reviews (id, bank_id, review, rating, review_date, source) VALUES (' ||
       id || ', ' || bank_id || ', ''' || REPLACE(review, '''', '''''') || ''', ' ||
       NVL(TO_CHAR(rating), 'NULL') || ', TO_DATE(''' || TO_CHAR(review_date, 'YYYY-MM-DD') || ''', ''YYYY-MM-DD''), ''' || REPLACE(source, '''', '''''') || ''');'
FROM reviews;

SPOOL OFF
EXIT

