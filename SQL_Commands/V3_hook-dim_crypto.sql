CREATE TABLE IF NOT EXISTS {target_schema}.dim_crypto
(
 crypto_id Serial  PRIMARY KEY NOT NULL,
 symbol VARCHAR,
 name VARCHAR  ,
 founder_creator VARCHAR,
 launch_date TIMESTAMP,
 type VARCHAR
);
CREATE INDEX IF NOT EXISTS idx_crypto_id {target_schema}.dim_crypto ON (crypto_id);
INSERT INTO {target_schema}.dim_crypto_id
    ( crypto_id,symbol,name,founder_creator, launch_date,type)
SELECT 
   	src_crypto.crypto_id,
    src_crypto.symbol,
    src_crypto.NAME,
    src_crypto.founder_creator
	src_crypto.launch_date 
	src_crypto.type
FROM {target_schema}.stg_src_crypto
ON CONFLICT (crypto_id)
DO UPDATE SET
 crypto_id =	src_crypto.crypto_id
 symbol = src_crypto.symbol
 name   =  src_crypto.NAME
 founder_creator =src_crypto.founder_creator
 launch_date =src_crypto.launch_date 
 type = src_crypto.type

