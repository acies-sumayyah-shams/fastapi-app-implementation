from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import psycopg2


my_app = FastAPI()

#Response that'll be returned while we hit the API
QUERY_INSERTED_SUCCESS_MESSAGE = "Insert query executed successfully."
QUERY_EXECUTED_SUCCESS_MESSAGE = "Query executed successfully."
FAILED_TO_ADD_MESSAGE = "Failed to add intern."
ADD_INTERN_SUCCESS_MESSAGE = "Added intern successfully."
DATABASE_ERROR_MESSAGE = "Database error"

#Queries
FETCH_ALL_INTERNS = """ select * from fastapi_demo.interns_details"""
INSERT_NEW_INTERN = """insert into fastapi_demo.interns_details
                    (name, mail_id, dob, college_name, description, hobbies)
                    values (%s, %s, %s, %s, %s, %s)"""

#DB config details
db_config = {
    "host": "localhost",
    "database": "fastapi_implementation",
    "user": "your_username",
    "password": "your_password",
}

#This defines the structure and type of data for the table
class AddNewInternBody(BaseModel):
    name: str
    mail_id: str
    dob: str
    college_name: str
    description: str 
    hobbies: str

    
if __name__ == "__main__":
    uvicorn.run("__main__:my_app", host="0.0.0.0", port=8000, reload=True)


#GET API

@my_app.get("/interns/fetchInternDetails")
async def get_interns():
    return fetch_interns_details()

def fetch_interns_details():
    intern_details, message = fetch_all_interns()
    return 200, message, intern_details

def fetch_all_interns():
    return execute_select(query=FETCH_ALL_INTERNS, values=()) 

def execute_select(query, values=None):   
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, values)
        rows = cursor.fetchall()
        return rows, QUERY_EXECUTED_SUCCESS_MESSAGE
    except psycopg2.Error as e:
        return None, DATABASE_ERROR_MESSAGE + f": {e}"
    
#POST API
@my_app.post("/interns/addNewIntern")
async def add_intern(body: AddNewInternBody):
    return add_new_intern(body)

def add_new_intern(body: AddNewInternBody):
    values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies)
    rows_affected, message = add_intern(values)
    if rows_affected < 0:
        return 500, message, FAILED_TO_ADD_MESSAGE
    else:
        return 200, message, ADD_INTERN_SUCCESS_MESSAGE

def add_intern(values):
    return execute_insert(query=INSERT_NEW_INTERN, values=values)

def execute_insert(query, values=None):   
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        rows_affected = cursor.rowcount
        return rows_affected, QUERY_INSERTED_SUCCESS_MESSAGE
    except psycopg2.Error as e:
        return None, DATABASE_ERROR_MESSAGE + f": {e}"
    

