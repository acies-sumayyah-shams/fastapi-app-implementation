from fastapi import APIRouter
from ..services.intern_service import InternsService
from ..models.add_new_intern_body import AddNewInternBody


#Routes to respective api
router = APIRouter()
interns_service = InternsService()

@router.get("/interns/fetchInternDetails")
async def get_interns():
    return interns_service.fetch_interns_details()

@router.post("/interns/addNewIntern")
async def add_intern(body: AddNewInternBody):
    return interns_service.add_new_intern(body)
