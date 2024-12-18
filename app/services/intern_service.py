from ..repositories.repository import InternsRepository
from ..models.add_new_intern_body import AddNewInternBody
from app import constants


#Takes care of how to implement each api
class InternsService:
    def __init__(self):
        self.intern_repo = InternsRepository()

    def fetch_interns_details(self):
        intern_details, message = self.intern_repo.fetch_all_interns()
        return 200, message, intern_details

    def add_new_intern(self, body: AddNewInternBody):
        values = (body.name, body.mail_id, body.dob, body.college_name, body.description, body.hobbies)
        rows_affected, message = self.intern_repo.add_intern(values)
        if rows_affected < 0:
            return 500, message, constants.FAILED_TO_ADD_MESSAGE
        else:
            return 200, message, constants.ADD_INTERN_SUCCESS_MESSAGE