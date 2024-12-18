
class InternsQueries:
    FETCH_ALL_INTERNS = """ select * from fastapi_demo.interns_details"""
    INSERT_NEW_INTERN = """insert into fastapi_demo.interns_details
                        (name, mail_id, dob, college_name, description, hobbies)
                        values (%s, %s, %s, %s, %s, %s)"""
