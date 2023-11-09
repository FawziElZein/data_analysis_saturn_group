CREATE TABLE IF NOT EXISTS target_schema.fct_crypto_tweets (
	created_at DATE,
	full_text TEXT,
	favorite_count INTEGER,
	reply_count INTEGER,
	retweet_count INTEGER,
	coin VARCHAR(20),
    current_coin_price DECIMAL,
	compound DOUBLE PRECISION,
	sentiment_type VARCHAR(20)
);


INSERT INTO target_schema.fct_crypto_tweets
(
	SELECT 
        created_at,
        full_text,
        favorite_count,
        reply_count,
        retweet_count, 
        unnest(string_to_array(substring(new_coins FROM 2 FOR LENGTH(new_coins)-2), ',')) AS coin,
        target_schema.get_current_coin_price(
            unnest(string_to_array(substring(new_coins FROM 2 FOR LENGTH(new_coins)-2), ',')),
            1,
            created_at) AS current_coin_price,
        compound,
        sentiment_type
    FROM target_schema.stg_crypto_db_crypto_tweets
)
