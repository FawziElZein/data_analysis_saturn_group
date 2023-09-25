CREATE TABLE IF NOT EXISTS target_schema.dim_time_bitcoin
(
    date TIMESTAMP PRIMARY KEY NOT NULL,
    high DECIMAL,
    low DECIMAL,
    open DECIMAL,
    close DECIMAL,
    volume DECIMAL
);

INSERT INTO target_schema.dim_time_bitcoin
(

    date TIMESTAMP PRIMARY KEY NOT NULL,
    high DECIMAL,
    low DECIMAL,
    open DECIMAL,
    close DECIMAL,
    volume DECIMAL
    FROM target_schema.stg_crypto_db_time_bitcoin
)

