CREATE TABLE IF NOT EXISTS target_schema.fct_market_cap
(
    till_day_of_year TIMESTAMP PRIMARY KEY NOT NULL,
    market_capitalization FLOAT
);

CREATE INDEX IF NOT EXISTS idx_till_day_of_year ON target_schema.fct_market_cap(till_day_of_year);


INSERT INTO target_schema.fct_market_cap
(
    SELECT
        till_day_of_year,
        CAST(market_capitalization AS FLOAT)
    FROM target_schema.stg_crypto_db_market_cap
)
ON CONFLICT (till_day_of_year)
DO UPDATE SET
        till_day_of_year = EXCLUDED.till_day_of_year,
        market_capitalization = EXCLUDED.market_capitalization;