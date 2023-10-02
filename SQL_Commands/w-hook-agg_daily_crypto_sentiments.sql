CREATE TABLE IF NOT EXISTS target_schema.agg_daily_crypto_sentiments(
    created_at DATE,
    coin VARCHAR(20),
	created_at_coin VARCHAR(200) PRIMARY KEY NOT NULL,
    total_favorite_count INTEGER,
    total_reply_count INTEGER,
    total_retweet_count INTEGER,
    avg_coumpound DOUBLE PRECISION,
    total_neutral INTEGER,
    total_positive INTEGER,
    total_negative INTEGER,
	current_price DECIMAL
);

CREATE INDEX IF NOT EXISTS idx_created_at_coin ON target_schema.agg_daily_crypto_sentiments(created_at_coin);

INSERT INTO target_schema.agg_daily_crypto_sentiments
(
SELECT
	created_at,
	coin,
	CONCAT(created_at,'-',coin) AS created_at_coin,
	SUM(favorite_count) AS total_favorite_count,
	SUM(reply_count) AS total_reply_count,
	SUM(retweet_count) AS total_retweet_count,
	AVG(compound) AS avg_coumpound,
	COUNT(
		CASE 
			WHEN sentiment_type = 'NEUTRAL' 
			THEN created_at
		END
	) AS Total_neutral,
	
	COUNT(
		CASE 
			WHEN sentiment_type = 'POSITIVE' 
			THEN created_at
		END
	) AS Total_positive,
	COUNT(
		CASE 
			WHEN sentiment_type = 'NEGATIVE' 
			THEN created_at
		END
	) AS Total_negative,
	current_coin_price

FROM target_schema.fct_crypto_tweets
GROUP BY
	created_at,coin,current_coin_price
)
ON CONFLICT(created_at_coin)
DO UPDATE SET
	total_favorite_count = EXCLUDED.total_favorite_count,
	total_reply_count = EXCLUDED.total_reply_count,
	total_retweet_count = EXCLUDED.total_retweet_count,
	avg_coumpound = EXCLUDED.avg_coumpound,
	total_neutral = EXCLUDED.total_neutral,
	total_positive = EXCLUDED.total_positive,
	total_negative = EXCLUDED.total_negative,
	current_price = EXCLUDED.current_price;