import os
from database_handler import return_query,execute_query, create_connection, close_connection,return_data_as_df
from pandas_data_handler import return_create_statement_from_df,return_insert_into_sql_statement_from_df,get_csv_into_df_list,get_online_csv_into_df_list
from lookups import ErrorHandling, PreHookSteps, InputTypes, SourceName,DestinationName,ETLStep,CsvUrlCoinsInfo,CsvUrlTweets,CoinsEnergyConsumption,CsvUrlHistoricalData
from logging_handler import show_error_message
from misc_handler import execute_sql_folder,create_insert_sql
import pandas as pd
import datetime
from dateutil.parser import parse

def parse_date_columns(dataframe):
    first_row = dataframe.iloc[0]
    for index,val in zip(first_row.index, first_row):
        try:
            parsed_date = parse(val, fuzzy=True)
            if isinstance(parsed_date, datetime.datetime):
                dataframe[index] = pd.to_datetime(dataframe[index])
        except Exception as e:
            suffix = str(e)
            error_prefix = ErrorHandling.DATE_CONVERSION_ERROR.value
            show_error_message(error_prefix,suffix)
    

def execute_prehook(sql_command_directory_path = './SQL_Commands'):
    try:
        db_session = create_connection()
        execute_sql_folder(db_session, sql_command_directory_path, ETLStep.PRE_HOOK, DestinationName.Datawarehouse)
        df_src_list ,df_src_titles = get_online_csv_into_df_list(CsvUrlHistoricalData)
        # df_src_list ,df_src_titles = get_online_csv_into_df_list(CsvUrlTweets)
        # df_ = pd.read_csv('dex_transactions_post_cleaning.csv')
        # parse_date_columns(df_)

        # df_.set_index(df_.columns[0],inplace=True)
        # df_src_list ,df_src_titles = [df_],['crypto_transactions']
        
        create_insert_sql(db_session, SourceName.CRYPTO_DB, df_src_list, df_src_titles,etl_step=ETLStep.PRE_HOOK)
        close_connection(db_session)
        return df_src_list,df_src_titles
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.PREHOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
