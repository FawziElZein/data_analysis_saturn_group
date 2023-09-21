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
    CREATE_STAGING_TABLES_ERROR = "Error creating staging tables"
    ETL_CHECKPOINT_ERROR = "Error creating ETL checkpoint"
    FUNCTION_NA = "Function not available"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"
    HOOK_SQL_ERROR = "Hook: SQL Error"
    DATE_CONVERSION_ERROR = "column is not a date format"
    RETURN_ETL_LAST_UPDATE_ERROR = "Error returning ETL last update"
    

class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    
class PandasFunctions(Enum):
    REMOVE_DUPLICATES = "remove duplicates values from data frame"
    REMOVE_NULLS = "remove nulls values from data frame"
    GET_BLANKS = "retreive rows having any cell with an empty value"
    GET_SHAPE = "retreive dimensions of the data frame"
    GET_LENGTH = "retreive the length of the data frame"
  
class PreHookSteps(Enum):
    EXECUTE_SQL_QUERY = "execute_sql_folder"

class SourceName(Enum):
    DVD_RENTAL = "dvd_rental"
    COLLEGE = "college"
    SUPER_STORE = "super_store"

class CsvUrl(Enum):
    ELON_MUSK_TWEETS = 'https://storage.googleapis.com/kagglesdsdata/datasets/3563626/6206522/Emusk_2021_tweets.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230920%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230920T144512Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=33c16d7667b7d7b016856e3955505b7261e058d88c026b6586cba7c78b30feda5839a21220bd5d29a69e73a978711eac8d92d908cc08005c72ad6535a9a545f64f852e814f8fcf89e9468834fbfcfe7119470bcc1c119553b86e3f8c6554b3df4f83a34df0558904041585a32c9f0ad5b349558e78f15b25eb2179a842feec84c90c2eade403058bec18c5b3491460fbccd91d166d9f912ec36599b3cc7cef9fe7945d98fc3ba56adf75c27af5b5e7a2838408da40e4692f7603ecf5ccbd27f1ac347291fa23b6be83e8581828915be54f02651fed30ff1d70a02befa2d39138d80205218f0424b274b6119b40f8d94b31d0cb7f8721144511e2df5434dc25a0' 
    BITCOIN_USD_HISTORICAL_DATA = 'https://www.coingecko.com/price_charts/export/1/usd.csv'
    

class SQLTablesToReplicate(Enum):
    RENTAL = "dvd_rental.rental"
    FILM = "dvd_rental.film"
    STUDENTS = "college.student"
    DIM_CUSTOMER = "super_store.dim_customer"
    DIM_LOCATION = "super_store.dim_location"
    DIM_PRODUCT = "super_store.dim_product"
    DIM_SALESPERSON = "super_store.dim_salesperson"
    FACT_PURCHASE = "super_store.fact_purchase"
    
class IncrementalField(Enum):
    RENTAL = "rental_last_update"
    FILM = "film_last_update"
    ACTOR = "actor_last_update"


class ETLStep(Enum):
    PRE_HOOK = 0
    HOOK = 1
