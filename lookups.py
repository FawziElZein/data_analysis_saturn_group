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
