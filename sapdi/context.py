from sapdi.client import SAPDIClient


class MCPContext:
    def __init__(self, config):
        self.sapdi = SAPDIClient(
            base_url=config["BASE_URL"],
            tenant=config["TENANT"],
            username=config["USERNAME"],
            password=config["PASSWORD"]
        )

        # optional: login at startup
        self.sapdi.login()
