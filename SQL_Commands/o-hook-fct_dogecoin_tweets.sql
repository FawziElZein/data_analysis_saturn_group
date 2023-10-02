CREATE TABLE IF NOT EXISTS target_schema.fct_doge_coin_tweets
(
    datetime TIMESTAMP PRIMARY KEY,
    tweet_id DOUBLE PRECISION,
    text TEXT,
    compound DOUBLE PRECISION,
    sentiment_type TEXT,
    current_price DECIMAL
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.fct_doge_coin_tweets(datetime);

INSERT INTO target_schema.fct_doge_coin_tweets
(
    SELECT
        datetime,
        tweet_id,
        text,
        compound,
        sentiment_type,
        target_schema.get_current_coin_price('DOGE',1,datetime)
    FROM target_schema.stg_crypto_db_elon_musk_tweets
)
ON CONFLICT (datetime)
DO UPDATE SET
        datetime = EXCLUDED.datetime,
        tweet_id = EXCLUDED.tweet_id,
        text = EXCLUDED.text,
        compound = EXCLUDED.compound,
        sentiment_type = EXCLUDED.sentiment_type;