import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=f"{os.getcwd()}\\app\\envs\\.env")

# Database configuration dictionary
db_config = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}
