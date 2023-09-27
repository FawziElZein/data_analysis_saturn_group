CREATE TABLE IF NOT EXISTS target_schema.fct_doge_coin_tweets
(
    datetime TIMESTAMP PRIMARY KEY,
    tweet_id DOUBLE PRECISION,
    text TEXT
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.fct_doge_coin_tweets(datetime);

INSERT INTO target_schema.fct_doge_coin_tweets
(
    SELECT
        datetime,
        tweet_id,
        text
    FROM target_schema.stg_crypto_db_elon_musk_tweets
)
ON CONFLICT (datetime)
DO UPDATE SET
        datetime = EXCLUDED.datetime,
        tweet_id = EXCLUDED.tweet_id,
        text = EXCLUDED.text;