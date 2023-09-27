CREATE TABLE IF NOT EXISTS target_schema.dim_time_tether
(
    date TIMESTAMP PRIMARY KEY NOT NULL,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    open DOUBLE PRECISION,
    close DOUBLE PRECISION,
    volume DOUBLE PRECISION,
    marketcap DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.dim_time_tether(date);

INSERT INTO target_schema.dim_time_tether
(
    SELECT
        date,
        high,
        low,
        open,
        close,
        volume,
        marketcap
    FROM target_schema.stg_crypto_db_tether_historical_price
)
ON CONFLICT (date)
DO UPDATE SET
    high = EXCLUDED.high,
    low = EXCLUDED.low,
    open = EXCLUDED.open,
    close = EXCLUDED.close,
    volume = EXCLUDED.volume,
    marketcap = EXCLUDED.marketcap;

