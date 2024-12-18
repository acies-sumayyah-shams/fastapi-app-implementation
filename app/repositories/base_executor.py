import psycopg2
from app import constants


#To establish db connection and execute respective query functions
class BaseExecutor:
    def __init__(self, db_config):
        self.db_config = db_config

    def execute_select(self, query, values=None):   
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)
            rows = cursor.fetchall()
            return rows, constants.QUERY_EXECUTED_SUCCESS_MESSAGE
        except psycopg2.Error as e:
            return None,  constants.DATABASE_ERROR_MESSAGE + f": {e}"
        
    def execute_insert(self, query, values=None):   
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            rows_affected = cursor.rowcount
            return rows_affected,  constants.QUERY_INSERTED_SUCCESS_MESSAGE
        except psycopg2.Error as e:
            return None,  constants.DATABASE_ERROR_MESSAGE + f": {e}"
    