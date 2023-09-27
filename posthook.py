from database_handler import execute_query, create_connection
import misc_handler
import lookups

def truncate_staging_tables(source_name, table_list, db_session):
    for table in table_list:
        dst_table = f"stg_{table}"
        truncate_query = f"""
        TRUNCATE TABLE IF EXISTS {dst_table}"""
        execute_query(db_session, truncate_query)



def execute_posthook():
    print("posthook")