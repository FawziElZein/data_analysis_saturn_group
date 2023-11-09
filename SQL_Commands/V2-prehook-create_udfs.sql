CREATE OR REPLACE FUNCTION target_schema.get_bitcoin_name(crypto_symbol TEXT)
RETURNS text AS
$$
DECLARE
    coin_name text;
BEGIN

    CASE TRIM(BOTH ' ' FROM crypto_symbol)
        WHEN 'BTC' THEN coin_name := 'bitcoin'; 
        WHEN 'ETH' THEN coin_name := 'ethereum'; 
        WHEN 'USDT' THEN coin_name := 'tether'; 
        WHEN 'BNB' THEN coin_name := 'binancecoin'; 
        WHEN 'XRP' THEN coin_name := 'xrp';
        WHEN 'LTC' THEN coin_name := 'litecoin'; 
        WHEN 'USDC' THEN coin_name := 'usdcoin'; 
        WHEN 'DOGE' THEN coin_name := 'dogecoin'; 
        WHEN 'TRX' THEN coin_name := 'tron'; 
        WHEN 'BUSD' THEN coin_name := 'binance_usd'; 
        ELSE coin_name := 'unknown';
    END CASE;
    
    RETURN coin_name;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION target_schema.get_current_coin_price(coin_symbol VARCHAR(50),amount DOUBLE PRECISION,date_time TIMESTAMP)
RETURNS DOUBLE PRECISION AS $$
DECLARE
	coin_name TEXT;
	query TEXT;
	price_result DOUBLE PRECISION;
BEGIN

	coin_name := target_schema.get_bitcoin_name(coin_symbol);
	IF coin_name !='unknown' THEN
	
		query:= '
			SELECT 
				(high+low)/2 AS mid_price
			FROM target_schema.dim_time_'||coin_name||'
			WHERE CAST(date AS DATE)= CAST('''||date_time||''' as DATE)';
		EXECUTE query INTO price_result;
	ELSE
		price_result :=NULL;
	END IF;
  RETURN ROUND(CAST(price_result * amount AS DECIMAL),5);
END;
$$ LANGUAGE plpgsql;