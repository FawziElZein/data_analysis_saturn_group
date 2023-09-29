CREATE TABLE IF NOT EXISTS target_schema.agg_transactions
(
    date TIMESTAMP PRIMARY KEY,
    total_buy INTEGER,
    total_sell INTEGER,
    total_swap INTEGER,
    top5_tokens_out TEXT,
    top5_tokens_in TEXT
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.agg_transactions(date);

WITH CTE_COINS_PER_BLOCK_NO_OUT AS(
	
	SELECT
		date_time,
		token_out,
		COUNT(id) AS number_of_coins_out
	FROM target_schema.fct_transactions
	GROUP BY
		date_time,token_out
	ORDER BY 
		date_time,number_of_coins_out DESC
),
CTE_TOP5_TRADED_COINS_OUT AS(
	SELECT
		date_time,
		STRING_AGG(coins_number,'/') AS top5_tokens_out
	FROM
	(
		SELECT
			date_time,
			CONCAT(token_out,':',CAST(number_of_coins_out AS TEXT)) AS coins_number,
			ROW_NUMBER() OVER(PARTITION BY date_time ORDER BY number_of_coins_out DESC) AS rank
		FROM
			CTE_COINS_PER_BLOCK_NO_OUT
	) AS partitioned_coins_counts
	WHERE
		rank<=5
	GROUP BY 
		date_time
),
CTE_COINS_PER_BLOCK_NO_IN AS(
	
	SELECT
		date_time,
		token_in,
		COUNT(id) AS number_of_coins_in
	FROM target_schema.fct_transactions
	GROUP BY
		date_time,token_in
	ORDER BY 
		date_time,number_of_coins_in DESC
),

CTE_TOP5_TRADED_COINS_IN AS(
	SELECT
		date_time,
		STRING_AGG(coins_number,'/') AS top5_tokens_in
	FROM
	(
		SELECT
			date_time,
			CONCAT(token_in,':',CAST(number_of_coins_in AS TEXT)) AS coins_number,
			ROW_NUMBER() OVER(PARTITION BY date_time ORDER BY number_of_coins_in DESC) AS rank
		FROM
			CTE_COINS_PER_BLOCK_NO_IN
	) AS partitioned_coins_counts
	WHERE
		rank<=5
	GROUP BY 
		date_time
),
CTE_ACTION_OPERATIONS AS (
SELECT
	date_time,
	COUNT(
		CASE 
			WHEN action = 'Buy' 
			THEN id
		END
		) AS Total_Buy,
	COUNT(
		CASE 
			WHEN action = 'Sell' 
			THEN id
		END
		) AS Total_Sell,
	COUNT(
		CASE 
			WHEN action = 'Swap' 
			THEN id
		END
		) AS Total_Swap
	
FROM target_schema.fct_transactions
GROUP BY
	date_time
)


INSERT INTO target_schema.agg_transactions
(
    SELECT
        CTE_ACTION_OPERATIONS.date_time,
        CTE_ACTION_OPERATIONS.total_buy,
        CTE_ACTION_OPERATIONS.total_sell,
        CTE_ACTION_OPERATIONS.total_swap,
        CTE_TOP5_TRADED_COINS_OUT.top5_tokens_out,
        CTE_TOP5_TRADED_COINS_IN.top5_tokens_in
    FROM CTE_ACTION_OPERATIONS
    INNER JOIN CTE_TOP5_TRADED_COINS_OUT
    ON CTE_ACTION_OPERATIONS.date_time = CTE_TOP5_TRADED_COINS_OUT.date_time
    INNER JOIN CTE_TOP5_TRADED_COINS_IN
    ON CTE_ACTION_OPERATIONS.date_time = CTE_TOP5_TRADED_COINS_IN.date_time
)
ON CONFLICT(date)
DO UPDATE SET
    date = EXCLUDED.date,
    total_buy = EXCLUDED.total_buy,
    total_sell = EXCLUDED.total_sell,
    total_swap = EXCLUDED.total_swap,
    top5_tokens_out = EXCLUDED.top5_tokens_out,
    top5_tokens_in = EXCLUDED.top5_tokens_in;