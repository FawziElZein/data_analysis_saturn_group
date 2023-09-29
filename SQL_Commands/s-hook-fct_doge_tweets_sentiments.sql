CREATE TABLE IF NOT EXISTS target_schema.fct_doge_tweets_sentiments
(
    date TIMESTAMP PRIMARY KEY,
    close DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    open DOUBLE PRECISION,
    volume DOUBLE PRECISION,
    adjclose DOUBLE PRECISION,
    changes text
);


CREATE INDEX IF NOT EXISTS idx_date ON target_schema.fct_doge_tweets_sentiments(date);

INSERT INTO target_schema.fct_doge_tweets_sentiments
(
    SELECT
        date,
        close,
        high,
        low,
        open,
        volume,
        adjclose,
        changes
    FROM target_schema.stg_crypto_db_doge_tweets_sentiments
)
ON CONFLICT (date)
DO UPDATE SET
        date = EXCLUDED.date,
        close = EXCLUDED.close,
        high = EXCLUDED.high,
        low = EXCLUDED.low,
        open = EXCLUDED.open,
        volume = EXCLUDED.volume,
        adjclose = EXCLUDED.adjclose,
        changes = EXCLUDED.changes;