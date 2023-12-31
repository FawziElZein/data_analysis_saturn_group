import os
from lookups import ErrorHandling,ETLStep,InputTypes,DateField,CsvUrlTweets
from database_handler import return_query,execute_query, create_connection, close_connection,return_data_as_df
from pandas_data_handler import return_create_statement_from_df,return_insert_into_sql_statement_from_df
from logging_handler import show_error_message
import pandas as pd

def return_staging_tables_as_list():
    tables = [str(table.name).lower() for table in DateField]
    return tables

    
def return_lookup_items_as_dict(lookup_item):
    enum_dict = {str(item.name).lower():item.value.replace(item.name.lower() + "_","") for item in lookup_item}
    return enum_dict


def return_tables_by_schema(schema_name):
    schema_tables = list()
    tables = [table.value for table in SQLTablesToReplicate]
    for table in tables:
        if table.split('.')[0] == schema_name:
            schema_tables.append(table.split('.')[1])
    return schema_tables

def execute_sql_folder(db_session, sql_command_directory_path, etl_step, target_schema):
    sql_files = [sqlfile for sqlfile in os.listdir(sql_command_directory_path) if sqlfile.endswith('.sql')]
    sorted_sql_files = sorted(sql_files, key=lambda x: int(x[1:x.index('-')]))
    counter = 0
    for sql_file in sorted_sql_files:
        counter+=1
        file_title = sql_file.split('-')
        if file_title[1] == etl_step.value:
            with open(os.path.join(sql_command_directory_path,sql_file), 'r') as file:
                sql_query = file.read()
                sql_query = sql_query.replace('target_schema', target_schema.value)
                return_val = execute_query(db_session= db_session, query= sql_query)
                if not return_val == ErrorHandling.NO_ERROR:
                    raise Exception(f"Error executing SQL File on = " +  str(sql_file))


def create_sql_staging_table_index(db_session,source_name, table_name, index_val):
    query = f"CREATE INDEX IF NOT EXISTS idx_{table_name}_{index_val} ON {source_name}.{table_name} ({index_val});"
    execute_query(db_session,query)

def create_insert_sql(db_session, source_name,df_source_list,df_titles,etl_step,etl_date = None):
    
    try:
        source_name = source_name.value
        for df_title, df_source in zip(df_titles,df_source_list):
            dst_table = f"stg_{source_name}_{df_title}"
            if etl_step == ETLStep.PRE_HOOK:
                
                create_stmt = return_create_statement_from_df(df_source, 'dw_reporting', dst_table)
                execute_query(db_session=db_session, query= create_stmt)

                index_name = df_source.index.name.replace(" ", "_").replace("-", "_")
                create_sql_staging_table_index(db_session, 'dw_reporting', dst_table, index_name)
            elif etl_step == ETLStep.HOOK:
                date_dict = return_lookup_items_as_dict(DateField)
                if date_dict.get(df_title)=='index':
                    staging_df = df_source[df_source.index>etl_date]
                else:
                    staging_df = df_source[df_source[date_dict.get(df_title)]>etl_date]
                if len(staging_df):
                    insert_stmt = return_insert_into_sql_statement_from_df(staging_df, 'dw_reporting', dst_table)
                    execute_query(db_session=db_session, query= insert_stmt)
        
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.CREATE_INSERT_STAGING_TABLES_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Error creating/insert into staging tables")


