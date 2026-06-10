import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("SAPDI_BASE_URL")
    PASSWORD = os.getenv("SAPDI_PASSWORD")
    TENANT = os.getenv("SAPDI_TENANT", "default")
    USERNAME = os.getenv("SAPDI_USERNAME")
    


if not Config.BASE_URL or not Config.USERNAME or not Config.PASSWORD:
    raise Exception("Missing SAP DI environment variables")
