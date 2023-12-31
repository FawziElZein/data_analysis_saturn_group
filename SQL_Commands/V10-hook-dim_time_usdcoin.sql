CREATE TABLE IF NOT EXISTS target_schema.dim_time_usdcoin
(
    date TIMESTAMP PRIMARY KEY NOT NULL,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    open DOUBLE PRECISION,
    close DOUBLE PRECISION,
    volume DOUBLE PRECISION,
    adjclose DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.dim_time_usdcoin(date);

INSERT INTO target_schema.dim_time_usdcoin
(
    SELECT
        formatted_date,
        high,
        low,
        open,
        close,
        volume,
        adjclose
    FROM target_schema.stg_crypto_db_usdcoin_historical_price
)
ON CONFLICT (date)
DO UPDATE SET
    high = EXCLUDED.high,
    low = EXCLUDED.low,
    open = EXCLUDED.open,
    close = EXCLUDED.close,
    volume = EXCLUDED.volume,
    adjclose = EXCLUDED.adjclose;

