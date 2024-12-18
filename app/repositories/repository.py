from ..config.config import db_config
from ..repositories.base_executor import BaseExecutor
from ..repositories.query import InternsQueries


#Interacts with the Database through queries and the base executor
class InternsRepository:
    def __init__(self):
        self.base_executor = BaseExecutor(db_config=db_config)

    def fetch_all_interns(self):
        return self.base_executor.execute_select(query=InternsQueries.FETCH_ALL_INTERNS, values=()) 
    
    def add_intern(self, values):
        return self.base_executor.execute_insert(query=InternsQueries.INSERT_NEW_INTERN, values=values)