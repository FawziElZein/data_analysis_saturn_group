from database_handler import execute_query, create_connection, close_connection,return_data_as_df
from pandas_data_handler import return_insert_into_sql_statement_from_df
from lookups import ErrorHandling,InputTypes,ETLStep,DestinationDatabase
from datetime import datetime
from misc_handler import execute_sql_folder, create_insert_sql
from logging_handler import show_error_message

def create_etl_checkpoint(db_session):
    try:
        query = """
            CREATE TABLE IF NOT EXISTS dw_reporting.etl_checkpoint
            (
                etl_last_run_date TIMESTAMP
            )
            """
        execute_query(db_session, query)
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.ETL_CHECKPOINT_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")

def insert_or_update_etl_checkpoint(db_session,does_etl_time_exists, etl_date = None):

    if does_etl_time_exists:

        status,status_message = ErrorHandling.ETL_UPDATE_CHECKPOINT_ERROR,"updating"
        insert_update_stmnt = f"UPDATE dw_reporting.etl_checkpoint SET etl_last_run_date = '{etl_date}'"

    else:

        status,status_message = ErrorHandling.ETL_INSERT_CHECKPOINT_ERROR,"inserting"
        insert_update_stmnt = f"INSERT INTO dw_reporting.etl_checkpoint (etl_last_run_date) VALUES ('{etl_date}')"

    try:
        execute_query(db_session, insert_update_stmnt)
    except Exception as e:
        suffix = str(error)
        error_prefix = status
        show_error_message(error_prefix.value, suffix)
        raise Exception(f"Error while {status_message} ETL checkpoint")

    
def return_etl_last_updated_date(db_session):

    does_etl_time_exists = False
    query = "SELECT etl_last_run_date FROM dw_reporting.etl_checkpoint ORDER BY etl_last_run_date DESC LIMIT 1"

    try:

        etl_df = return_data_as_df(
            file_executor= query,
            input_type= InputTypes.SQL,
            db_session= db_session
        )
        if len(etl_df) == 0:
            return_date = datetime(1992,6,19) 
        else:
            return_date = etl_df['etl_last_run_date'].iloc[0]
            does_etl_time_exists = True
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.RETURN_ETL_LAST_UPDATE_ERROR
        show_error_message(error_prefix.value, suffix)
    finally:
        return return_date,does_etl_time_exists

def execute_hook(df_src_list,df_src_titles):
    try:
        db_session = create_connection()
        create_etl_checkpoint(db_session)
        etl_date, does_etl_time_exists = return_etl_last_updated_date(db_session)
        create_insert_sql(db_session,DestinationDatabase.DATABASE_NAME,df_src_list,df_src_titles, ETLStep.HOOK, etl_date)
        
        execute_sql_folder(db_session, './SQL_Commands', ETLStep.HOOK, DestinationDatabase.SCHEMA_NAME)
        #last step
        insert_or_update_etl_checkpoint(db_session, does_etl_time_exists,datetime.now())
        close_connection(db_session)
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.HOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
        
