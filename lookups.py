from enum import Enum


class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    CREATE_TABLE_ERROR = "Error creating new table"
    INSERT_INTO_TABLE_ERROR = "Error inserting into table"
    STAGING_DATA_ERROR = "Error staging recent data"
    CREATE_INSERT_STAGING_TABLES_ERROR = "Error creating/inserting into staging tables"
    ETL_CHECKPOINT_ERROR = "Error creating ETL checkpoint"
    ETL_INSERT_CHECKPOINT_ERROR = "Error inserting ETL checkpoint"
    ETL_UPDATE_CHECKPOINT_ERROR = "Error updating ETL checkpoint"
    FUNCTION_NA = "Function not available"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"
    HOOK_SQL_ERROR = "Hook: SQL Error"
    DATE_CONVERSION_ERROR = "Warning: column is not a date format"
    RETURN_ETL_LAST_UPDATE_ERROR = "Error returning ETL last update"
    

class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    HTTP = "Http"
    


class CsvUrlCoinsInfo(Enum):
    COINS_INFO = [0,'https://storage.googleapis.com/csv_links/cryptocurrency-coins-data-info.csv-2.csv']

class CsvUrlTweets(Enum):
    ELON_MUSK_TWEETS = [0,'https://storage.googleapis.com/csv_links/elon_musk_tweets_clean_data.csv','Text'] 
    CRYPTO_TWEETS = [0,'https://storage.googleapis.com/csv_links/dataset_52_person_tweets.csv','full_text']

class CoinsEnergyConsumption(Enum):
    BITCOIN_ENERGY_CONSUMPTION = [0,'https://storage.googleapis.com/csv_links/btc_energy_consumption.csv']

class CsvUrlHistoricalData(Enum):
    CRYPTO_TRANSACTIONS = [0,'https://storage.googleapis.com/csv_links/dex_transactions_post_cleaning.csv']
    MARKET_CAP = [0,'https://storage.googleapis.com/csv_links/market_capital_of_cryptocuurency_from_2009_till_2023.csv']

class DestinationDatabase(Enum):
    SCHEMA_NAME = "dw_reporting"
    DATABASE_NAME = "crypto_db"


class IncrementalField(Enum):
    COINS_INFO = "coins_info_Launch date"
    ELON_MUSK_TWEETS = "elon_musk_tweets_index"
    DATASET_MUTLI_COINS_TWEETS = "dataset_multi_coins_tweets_created_at"
    BITCOIN_HISTORICAL_PRICE = "bitcoin_historical_price_index"
    ETHEREUM_HISTORICAL_PRICE = "ethereum_historical_price_index"
    TETHER_HISTORICAL_PRICE = "tether_historical_price_index"
    BINANCECOIN_HISTORICAL_PRICE = "binancecoin_historical_price_index"
    XRP_HISTORICAL_PRICE = "xrp_historical_price_index"
    LITECOIN_HISTORICAL_PRICE = "litecoin_historical_price_index"
    USDCOIN_HISTORICAL_PRICE = "usdcoin_historical_price_index"
    DOGECOIN_HISTORICAL_PRICE = "dogecoin_historical_price_index"
    TRON_HISTORICAL_PRICE = "tron_historical_price_index"
    BINANCE_USD_HISTORICAL_PRICE = "binance_usd_historical_price_index"
    CRYPTO_TRANSACTIONS = "crypto_transactions_Date Time"
    BITCOIN_ENERGY_CONSUMPTION = "bitcoin_energy_consumption_index"
    BITCOIN_ABBREVIATION = "bitcoin_abbreviation_Abbrev"
    CRYPTO_TWEETS = "crypto_tweets_created_at"
    MARKET_CAP = "market_cap_index"

class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"
