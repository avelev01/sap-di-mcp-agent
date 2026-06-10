from sapdi.client import SAPDIClient
from sapdi.config import Config


class MCPContext:
    def __init__(self):
        self.sapdi = SAPDIClient(
            base_url=Config.BASE_URL,
            password=Config.PASSWORD,
            tenant=Config.TENANT,
            username=Config.USERNAME
            
        )

        self.sapdi.login()
