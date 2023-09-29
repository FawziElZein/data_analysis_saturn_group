from pandas_data_handler import return_create_statement_from_df,return_insert_into_sql_statement_from_df,get_csv_into_df_list,get_online_csv_into_df_list
from lookups import ErrorHandling, PreHookSteps, InputTypes,DestinationDatabase,ETLStep,CsvUrlCoinsInfo,CsvUrlTweets,CoinsEnergyConsumption,CsvUrlHistoricalData
from database_handler import return_query,execute_query, create_connection, close_connection,return_data_as_df
from misc_handler import execute_sql_folder,create_insert_sql
from crypto_historical_price import get_historical_prices
from logging_handler import show_error_message
import pandas as pd
import datetime
import os


def execute_prehook(sql_command_directory_path = './SQL_Commands'):
    try:

        db_session = create_connection()
        execute_sql_folder(db_session, sql_command_directory_path, ETLStep.PRE_HOOK, DestinationDatabase.SCHEMA_NAME)
        df_crypto_prices,df_crypto_titles = get_historical_prices()
        df_online_src_content ,df_online_src_titles = get_online_csv_into_df_list(CsvUrlCoinsInfo,CsvUrlTweets,CoinsEnergyConsumption,CsvUrlHistoricalData)
        
        df_src_content = df_crypto_prices + df_online_src_content
        df_src_titles = df_crypto_titles + df_online_src_titles

        create_insert_sql(db_session, DestinationDatabase.DATABASE_NAME, df_src_content, df_src_titles,etl_step=ETLStep.PRE_HOOK)
        close_connection(db_session)
        return df_src_content,df_src_titles
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.PREHOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
