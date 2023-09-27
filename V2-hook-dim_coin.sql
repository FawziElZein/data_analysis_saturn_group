CREATE TABLE IF NOT EXISTS target_schema.dim_coin
(

    symbol VARCHAR(10) PRIMARY KEY NOT NULL,
    name VARCHAR(20),
    founder VARCHAR(200),
    launch_date TIMESTAMP,
    security VARCHAR(200),
    strengths TEXT,
    weaknesses TEXT
);
CREATE INDEX IF NOT EXISTS idx_symbol  ON target_schema.dim_coin(symbol);

INSERT INTO target_schema.dim_coin
(
    SELECT
        ï»¿symbol,
        name,
        founder,
        launch_date,
        security,
        strengths,
        weaknesses
    FROM target_schema.stg_crypto_db_coins_info
)
ON CONFLICT (symbol)
DO UPDATE SET
    name = EXCLUDED.name,
    founder = EXCLUDED.founder,
    launch_date = EXCLUDED.launch_date,
    security = EXCLUDED.security,
    strengths = EXCLUDED.strengths,
    weaknesses = EXCLUDED.weaknesses;



