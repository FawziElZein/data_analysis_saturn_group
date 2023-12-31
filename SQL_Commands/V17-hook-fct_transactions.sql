CREATE TABLE IF NOT EXISTS target_schema.fct_transactions
(
    id INT PRIMARY KEY NOT NULL,
    txn_hash VARCHAR(255),
    block_no INT,
    date_time TIMESTAMP,
    action VARCHAR(50),
    amount_out DOUBLE PRECISION,
    token_out VARCHAR(50),
    price_out DECIMAL,
    amount_in DOUBLE PRECISION,
    token_in VARCHAR(50),
    price_in DECIMAL,
    swapped_rate DOUBLE PRECISION,
    dex VARCHAR(50)
);

CREATE INDEX IF NOT EXISTS idx_id ON target_schema.fct_transactions(id);

INSERT INTO target_schema.fct_transactions
(
    SELECT
        id,
        txn_hash,
        block_no,
        date_time,
        action,
        amount_out,
        token_out,
        target_schema.get_current_coin_price(transactions.token_out,amount_out,transactions.date_time) AS price_out,
        amount_in,
        token_in,
        target_schema.get_current_coin_price(transactions.token_in,amount_in,transactions.date_time) AS price_in,
        CAST(swapped_rate AS DOUBLE PRECISION),
        dex
    FROM target_schema.stg_crypto_db_crypto_transactions AS transactions
)
ON CONFLICT (id)
DO UPDATE SET
    txn_hash = EXCLUDED.txn_hash,
    block_no = EXCLUDED.block_no,
    date_time = EXCLUDED.date_time,
    action = EXCLUDED.action,
    amount_out = EXCLUDED.amount_out,
    token_out = EXCLUDED.token_out,
    price_out = EXCLUDED.price_out,
    amount_in = EXCLUDED.amount_in,
    token_in = EXCLUDED.token_in,
    price_in = EXCLUDED.price_in,
    swapped_rate = EXCLUDED.swapped_rate,
    dex = EXCLUDED.dex;
