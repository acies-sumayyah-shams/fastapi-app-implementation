from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from app.routers.interns_router import router  

load_dotenv('.env')

my_app = FastAPI()
my_app.include_router(router = router)
    
if __name__ == "__main__":
    uvicorn.run("__main__:my_app", host="0.0.0.0", port=int(os.getenv('API_PORT')), reload=True)
