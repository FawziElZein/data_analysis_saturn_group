from database_handler import execute_query, create_connection
import misc_handler
from lookups import DestinationDatabase

def truncate_staging_tables(source_name,schema_name, table_list, db_session):
    for table in table_list:
        dst_table = f"stg_{source_name.value}_{table}"
        # print("dst_table",dst_table)
        truncate_query = f"""
        DO $$ 
        BEGIN
            IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name.value}' AND table_name = '{dst_table}') THEN
            TRUNCATE TABLE {schema_name.value}.{dst_table};
                RAISE NOTICE 'Table truncated successfully.';
            ELSE
                RAISE NOTICE 'Table does not exist.';
            END IF;
        END $$;
            """
        # print(truncate_query)
        execute_query(db_session, truncate_query)



def execute_posthook():
    db_session = create_connection()
    tables = misc_handler.return_staging_tables_as_list()
    truncate_staging_tables(DestinationDatabase.DATABASE_NAME,DestinationDatabase.SCHEMA_NAME, tables, db_session)
    # # fragment_indexes_if_needed()
    # # fragmentation_for_indexes()
