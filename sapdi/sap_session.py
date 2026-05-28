import requests
from sapdi.config import Config


class SAPDISession:
    """
    SAP DI session manager for MCP agents.
    Handles:
    - login
    - token storage
    - automatic retry on 401
    - GET/POST API abstraction
    """

    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.logged_in = False
        self.base_url = Config.SAP_DI_BASE_URL

    # -------------------------
    # LOGIN
    # -------------------------
    def login(self):
        url = f"{self.base_url}{Config.SAP_DI_API_PREFIX}/auth/login"

        payload = {
            "tenant": Config.SAP_DI_TENANT,
            "username": Config.SAP_DI_USERNAME,
            "password": Config.SAP_DI_PASSWORD
        }

        response = self.session.post(
            url,
            json=payload,
            verify=Config.SAP_DI_VERIFY_SSL
        )

        if response.status_code != 200:
            raise Exception(
                f"SAP DI login failed [{response.status_code}]: {response.text}"
            )

        data = response.json()

        self.token = data.get("access_token")

        if not self.token:
            raise Exception("No access_token returned from SAP DI")

        # Attach token globally
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        })

        self.logged_in = True
        return data

    # -------------------------
    # ENSURE LOGIN
    # -------------------------
    def ensure_login(self):
        if not self.logged_in or not self.token:
            self.login()

    # -------------------------
    # INTERNAL REQUEST HANDLER
    # -------------------------
    def _request(self, method, path, **kwargs):
        self.ensure_login()

        url = f"{self.base_url}{path}"

        response = self.session.request(
            method,
            url,
            verify=Config.SAP_DI_VERIFY_SSL,
            **kwargs
        )

        # Handle expired token
        if response.status_code == 401:
            self.login()
            response = self.session.request(
                method,
                url,
                verify=Config.SAP_DI_VERIFY_SSL,
                **kwargs
            )

        response.raise_for_status()

        # Return JSON if possible
        try:
            return response.json()
        except Exception:
            return response.text

    # -------------------------
    # PUBLIC METHODS
    # -------------------------
    def get(self, path, params=None):
        return self._request("GET", path, params=params)

    def post(self, path, json=None):
        return self._request("POST", path, json=json)