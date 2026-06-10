import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("SAPDI_BASE_URL")
    TENANT = os.getenv("SAPDI_TENANT", "default")
    USERNAME = os.getenv("SAPDI_USERNAME")
    PASSWORD = os.getenv("SAPDI_PASSWORD")
