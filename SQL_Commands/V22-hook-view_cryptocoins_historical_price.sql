-- Crypto coins informations View

DROP VIEW IF EXISTS target_schema.vw_crypto_coins_info;

CREATE VIEW target_schema.vw_crypto_coins_info AS
	SELECT
		symbol,
		name,
		founder,
		launch_date,
		security,
		usage,
		strengths,
		weaknesses,
		country
	FROM target_schema.dim_coin;

-- Cryto historical price View

DROP VIEW IF EXISTS target_schema.vw_cryptocoins_historical_price;

CREATE VIEW target_schema.vw_cryptocoins_historical_price AS
(
	SELECT
		date,
		'BUSD' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_binance_usd
)
UNION
(
	SELECT
		date,
		'BNB' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_binancecoin
)
UNION
(
	SELECT
		date,
		'BTC' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_bitcoin
)
UNION 
(
	SELECT
		date,
		'DOGE' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_dogecoin
)
UNION
(
	SELECT
		date,
		'ETH' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_ethereum
)
UNION
(
	SELECT
		date,
		'LTC' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_litecoin
)
UNION
(
	SELECT
		date,
		'USDT' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_tether
)
UNION
(
	SELECT
		date,
		'TRX' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_tron
)
UNION
(
	SELECT
		date,
		'USDC' AS symbol,
		high,
		low,
		open,
		close,
		volume,
		adjclose
	FROM dw_reporting.dim_time_usdcoin
);

-- Market Capitalization View

DROP VIEW IF EXISTS target_schema.vw_market_capitalization;

CREATE VIEW target_schema.vw_market_capitalization AS
SELECT
	till_day_of_year,
    market_capitalization
FROM target_schema.fct_market_cap;

-- Daily Crypto Tweets sentiment View

DROP VIEW IF EXISTS target_schema.vw_daily_crypto_tweets_sentiment_analysis;

CREATE VIEW target_schema.vw_daily_crypto_tweets_sentiment_analysis AS
SELECT
	created_at,
    coin,
	created_at_coin,
    total_favorite_count,
    total_reply_count,
    total_retweet_count,
    avg_coumpound,
    total_neutral,
    total_positive,
    total_negative,
	current_price
FROM target_schema.agg_daily_crypto_sentiments;

-- Fact Transactions View

DROP VIEW IF EXISTS target_schema.vw_daily_transactions_per_coin;

CREATE VIEW target_schema.vw_daily_transactions_per_coin AS
SELECT
	id,
    txn_hash,
    block_no,
    date_time,
    action,
    amount_out,
    token_out,
    price_out,
    amount_in,
    token_in,
    price_in,
    swapped_rate,
    dex
FROM target_schema.fct_transactions;

-- Daily Transactions View

DROP VIEW IF EXISTS target_schema.vw_daily_transactions;

CREATE VIEW target_schema.vw_daily_transactions AS
SELECT
    date,
    total_buy,
    total_sell,
    total_swap,
    top5_tokens_out,
    top5_tokens_in
FROM target_schema.agg_daily_transactions;

-- Daily doge coin tweets sentiment View

DROP VIEW IF EXISTS target_schema.vw_daily_doge_coin_tweets_sentiment_analysis;

CREATE VIEW target_schema.vw_daily_doge_coin_tweets_sentiment_analysis AS 

SELECT
	datetime,
    tweet_id,
	datetime_tweet_id,
    average_compound,
	total_neutral,
	total_positive,
	total_negative,
	current_price
FROM target_schema.agg_daily_doge_coin_sentiments;


-- Bitcoin energy consumption View

DROP VIEW IF EXISTS target_schema.vw_bitcoin_energy_consumption;

CREATE VIEW target_schema.vw_bitcoin_energy_consumption AS

SELECT
	date,
    BTCENEMAX,
    BTCENEMIN,
    BTCENEGUE,	
    BTCEMI_MAX,
    BTCEMI_MIN,
    BTCEMI_GUE,
    BTCOAL_MAX,
    BTCOAL_MIN,
    BTCOAL_GUE,
    BTCOIL_MAX,
    BTCOIL_MIN,
    BTCOIL_GUE,
    BTCGAS_MAX,
    BTCGAS_MIN,
    BTCGAS_GUE
FROM target_schema.fct_bitcoin_energy_consumption;

