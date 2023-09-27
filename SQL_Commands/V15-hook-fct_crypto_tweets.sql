CREATE TABLE IF NOT EXISTS target_schema.fct_crypto_tweets
(
    tweet_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP,
    favorite_count INT,
    full_text TEXT,
    reply_count INT,
    retweet_count INT,
    new_coins TEXT
);

CREATE INDEX IF NOT EXISTS idx_tweet_id ON target_schema.fct_crypto_tweets(tweet_id);

INSERT INTO target_schema.fct_crypto_tweets
(
    SELECT
        tweet_id,
        created_at,
        favorite_count,
        full_text,
        reply_count,
        retweet_count,
        new_coins
    FROM target_schema.stg_crypto_db_crypto_tweets
)
ON CONFLICT (tweet_id)
DO UPDATE SET
        tweet_id = EXCLUDED.tweet_id,
        created_at = EXCLUDED.created_at,
        favorite_count = EXCLUDED.favorite_count,
        full_text = EXCLUDED.full_text,
        reply_count = EXCLUDED.reply_count,
        retweet_count = EXCLUDED.retweet_count,
        new_coins = EXCLUDED.new_coins;