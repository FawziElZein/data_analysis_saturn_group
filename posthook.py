from database_handler import execute_query, create_connection
import misc_handler
from lookups import DestinationDatabase

def truncate_staging_tables(source_name,schema_name, table_list, db_session):
    for table in table_list:
        dst_table = f"stg_{source_name.value}_{table}"
        truncate_query = f"""
        DO $$ 
        DECLARE
            index_to_drop TEXT;
        BEGIN
            IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name.value}' AND table_name = '{dst_table}') THEN
                TRUNCATE TABLE {schema_name.value}.{dst_table};
                RAISE NOTICE 'Table truncated successfully.';
                SELECT 
                    CONCAT('{schema_name.value}.',indexname) 
                INTO index_to_drop
                FROM pg_indexes 
                WHERE tablename = '{dst_table}'
                AND SUBSTRING(indexname FROM 1 FOR 4) = 'idx_';
                IF index_to_drop IS NOT NULL THEN
                    EXECUTE 'DROP INDEX ' || index_to_drop;
                ELSE 
                    RAISE NOTICE 'Index not found';
                END IF;
            ELSE
                RAISE NOTICE 'Table does not exist.';
            END IF;
        END $$;
            """
        execute_query(db_session, truncate_query)



def execute_posthook():
    db_session = create_connection()
    tables = misc_handler.return_staging_tables_as_list()
    truncate_staging_tables(DestinationDatabase.DATABASE_NAME,DestinationDatabase.SCHEMA_NAME, tables, db_session)
