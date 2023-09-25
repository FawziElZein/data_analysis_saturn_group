CREATE TABLE IF NOT EXISTS target_schema.dim_time_binance_usd
(
    date TIMESTAMP PRIMARY KEY NOT NULL,
    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    adj_close DOUBLE PRECISION,
    volume DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.dim_time_binance_usd(date);

INSERT INTO target_schema.dim_time_binance_usd
(
    SELECT
        date,
        open,
        high,
        low,
        close,
        adj_close,
        volume
    FROM target_schema.stg_crypto_db_binance_usd_historical_price
)
ON CONFLICT (date)
DO UPDATE SET
    open = EXCLUDED.open,
    high = EXCLUDED.high,
    low = EXCLUDED.low,
    close = EXCLUDED.close,
    adj_close = EXCLUDED.adj_close,
    volume = EXCLUDED.volume;