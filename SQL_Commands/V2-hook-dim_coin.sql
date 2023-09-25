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

INSERT INTO target_schema.dim_coin
(
    SELECT
        symbol,
        ï»¿Name,
        founder,
        launch_date,
        security,
        strengths,
        weaknesses
    FROM target_schema.stg_crypto_db_coins_info
)



