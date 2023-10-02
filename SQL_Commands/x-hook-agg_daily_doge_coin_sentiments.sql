CREATE TABLE target_schema.agg_daily_doge_coin_sentiments(
    datetime DATE,
    tweet_id DOUBLE PRECISION,
	datetime_tweet_id VARCHAR(200) PRIMARY KEY NOT NULL,
    average_compound DOUBLE PRECISION,
	total_neutral INTEGER,
	total_positive INTEGER,
	total_negative INTEGER,
	current_price DECIMAL
);

CREATE INDEX IF NOT EXISTS idx_datetime_tweet_id ON target_schema.agg_daily_doge_coin_sentiments(datetime_tweet_id);

INSERT INTO target_schema.agg_daily_doge_coin_sentiments
(
SELECT
	CAST(datetime AS DATE),
	tweet_id,
	CONCAT(CAST(datetime AS DATE),'-',tweet_id) AS datetime_tweet_id,
	AVG(compound) AS average_compound,
	COUNT(
		CASE 
			WHEN sentiment_type = 'NEUTRAL' 
			THEN datetime
		END
	) AS total_neutral,
	
	COUNT(
		CASE 
			WHEN sentiment_type = 'POSITIVE' 
			THEN datetime
		END
	) AS total_positive,
	COUNT(
		CASE 
			WHEN sentiment_type = 'NEGATIVE' 
			THEN datetime
		END
	) AS total_negative,
	current_price
FROM target_schema.fct_doge_coin_tweets
GROUP BY 
	CAST(datetime AS DATE),tweet_id,current_price
ORDER BY CAST(datetime AS DATE)
)

ON CONFLICT(datetime_tweet_id)
DO UPDATE SET
    average_compound = EXCLUDED.average_compound,
    total_neutral = EXCLUDED.total_neutral,
	total_positive = EXCLUDED.total_positive,
	total_negative = EXCLUDED.total_negative,
	current_price = EXCLUDED.current_price;