from sapdi.client import SAPDIClient
from config import Config


class MCPContext:
    def __init__(self):
        self.sapdi = SAPDIClient(
            base_url=Config.BASE_URL,
            tenant=Config.TENANT,
            username=Config.USERNAME,
            password=Config.PASSWORD
        )

        self.sapdi.login()
