CREATE TABLE "dim_crypto" (
  "crypto_id" SERIAL PRIMARY KEY,
  "symbol" VARCHAR(10),
  "name" VARCHAR(255),
  "founder_creator" VARCHAR(255),
  "launch_date" DATE,
  "type" VARCHAR(255)
);

CREATE TABLE "dim_crypto_tech" (
  "symbol" VARCHAR(10),
  "Technological_features" text,
  "dvantages_over_bitcoin" text
);

CREATE TABLE "fct_btc_footprint" (
  "abbrev" VARCHAR(255),
  "date" date,
  "foot" print
);

CREATE TABLE "dim_btc_footprint" (
  "abbrev" VARCHAR(255) PRIMARY KEY,
  "meaning" text,
  "unit" VARCHAR(10)
);

CREATE TABLE "Fct_Sentiment_Analysis" (
  "date" DATE,
  "crypto_id" INT,
  "sentiment_score" NUMERIC,
  "source" VARCHAR(255),
  "sentiment_text" TEXT
);

CREATE TABLE "FCT_TWEETS" (
  "crypto_id" INT,
  "NAME" VARCHAR(255),
  "DATE" DATE,
  "NUMBER_OF_TWEETS" INT
);

CREATE TABLE "Dim_TimeDimension" (
  "date" DATE,
  "crypto_id" INT,
  "symbol" VARCHAR(10),
  "high" NUMERIC,
  "low" NUMERIC,
  "open" NUMERIC,
  "close" NUMERIC,
  "volume" NUMERIC,
  "market_cap" NUMERIC
);

CREATE TABLE "transaction" (
  "txn_hash" VARCHAR(255) PRIMARY KEY,
  "block_no" INT,
  "unix_timestamp" BIGINT,
  "date_time_utc" TIMESTAMP,
  "action" VARCHAR(50),
  "amount_out" NUMERIC,
  "token_out" VARCHAR(255),
  "amount_in" NUMERIC,
  "token_in" VARCHAR(255),
  "swapped_rate" NUMERIC,
  "swapped_pair" VARCHAR(255),
  "dex" VARCHAR(255)
);

CREATE TABLE "agg_monthly_coin_price" (
  "month" DATE,
  "crypto_id" INT,
  "symbol" VARCHAR(10),
  "monthly_open" NUMERIC,
  "monthly_close" NUMERIC,
  "monthly_high" NUMERIC,
  "monthly_low" NUMERIC,
  "monthly_volume" NUMERIC,
  "monthly_variance" NUMERIC,
  "monthly_std_dev" NUMERIC
);

CREATE TABLE "agg_yearly_coin_price" (
  "year" DATE,
  "crypto_id" INT,
  "symbol" VARCHAR(10),
  "yearly_open" NUMERIC,
  "yearly_close" NUMERIC,
  "yearly_high" NUMERIC,
  "yearly_low" NUMERIC,
  "yearly_volume" NUMERIC,
  "yearly_variance" NUMERIC,
  "yearly_std_dev" NUMERIC
);

ALTER TABLE "dim_crypto_tech" ADD FOREIGN KEY ("symbol") REFERENCES "dim_crypto" ("symbol");

ALTER TABLE "fct_btc_footprint" ADD FOREIGN KEY ("abbrev") REFERENCES "dim_btc_footprint" ("abbrev");

ALTER TABLE "FCT_TWEETS" ADD FOREIGN KEY ("crypto_id") REFERENCES "dim_crypto" ("crypto_id");

ALTER TABLE "Dim_TimeDimension" ADD FOREIGN KEY ("crypto_id") REFERENCES "dim_crypto" ("crypto_id");

ALTER TABLE "Fct_Sentiment_Analysis" ADD FOREIGN KEY ("crypto_id") REFERENCES "dim_crypto" ("crypto_id");

ALTER TABLE "agg_monthly_coin_price" ADD FOREIGN KEY ("crypto_id") REFERENCES "dim_crypto" ("crypto_id");

ALTER TABLE "agg_yearly_coin_price" ADD FOREIGN KEY ("crypto_id") REFERENCES "dim_crypto" ("crypto_id");
