CREATE TABLE IF NOT EXISTS target_schema.fct_bitcoin_energy_consumption(
    date TIMESTAMP PRIMARY KEY,
    BTCENEMAX DOUBLE PRECISION,
    BTCENEMIN DOUBLE PRECISION,
    BTCENEGUE DOUBLE PRECISION,	
    BTCEMI_MAX DOUBLE PRECISION,
    BTCEMI_MIN DOUBLE PRECISION,
    BTCEMI_GUE DOUBLE PRECISION,
    BTCOAL_MAX DOUBLE PRECISION,
    BTCOAL_MIN DOUBLE PRECISION,
    BTCOAL_GUE DOUBLE PRECISION,
    BTCOIL_MAX DOUBLE PRECISION,
    BTCOIL_MIN DOUBLE PRECISION,
    BTCOIL_GUE DOUBLE PRECISION,
    BTCGAS_MAX DOUBLE PRECISION,
    BTCGAS_MIN DOUBLE PRECISION,
    BTCGAS_GUE DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS idx_date ON target_schema.fct_bitcoin_energy_consumption(date);

INSERT INTO target_schema.fct_bitcoin_energy_consumption
(
    SELECT
        ï»¿date,
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
    FROM target_schema.stg_crypto_db_bitcoin_energy_consumption

)
ON CONFLICT (date)
DO UPDATE SET
    date = EXCLUDED.date,
    BTCENEMAX = EXCLUDED.BTCENEMAX,
    BTCENEMIN = EXCLUDED.BTCENEMIN,
    BTCENEGUE = EXCLUDED.BTCENEGUE,	
    BTCEMI_MAX = EXCLUDED.BTCEMI_MAX,
    BTCEMI_MIN = EXCLUDED.BTCEMI_MIN,
    BTCEMI_GUE = EXCLUDED.BTCEMI_GUE,
    BTCOAL_MAX = EXCLUDED.BTCOAL_MAX,
    BTCOAL_MIN = EXCLUDED.BTCOAL_MIN,
    BTCOAL_GUE = EXCLUDED.BTCOAL_GUE,
    BTCOIL_MAX = EXCLUDED.BTCOIL_MAX,
    BTCOIL_MIN = EXCLUDED.BTCOIL_MIN,
    BTCOIL_GUE = EXCLUDED.BTCOIL_GUE,
    BTCGAS_MAX = EXCLUDED.BTCGAS_MAX,
    BTCGAS_MIN = EXCLUDED.BTCGAS_MIN,
    BTCGAS_GUE = EXCLUDED.BTCGAS_GUE;