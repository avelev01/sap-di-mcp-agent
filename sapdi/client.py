import requests


class SAPDIClient:
    def __init__(self, base_url: str, tenant: str, username: str, password: str):
        self.base_url = base_url.rstrip("/")
        self.tenant = tenant
        self.username = username
        self.password = password

        self.session = requests.Session()
        self.logged_in = False

    # -------------------------
    # STEP 1: bootstrap cookies
    # -------------------------
    def _bootstrap(self):
        self.session.get(
            f"{self.base_url}/login/?tenant={self.tenant}",
            verify=False
        )

    # -------------------------
    # LOGIN
    # -------------------------
    def login(self):
        self._bootstrap()

        resp = self.session.post(
            f"{self.base_url}/api/login/v2/finalize",
            json={
                "password": self.password
                "tenant": self.tenant,
                "username": self.username,
                
            },
            headers={
                "Content-Type": "application/json",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": self.base_url,
                "Referer": f"{self.base_url}/login/"
            },
            verify=False
        )

        if resp.status_code != 200:
            raise Exception(f"Login failed: {resp.text}")

        cookies = self.session.cookies.get_dict()

        if "vsystem-session-id" not in cookies:
            raise Exception("Login succeeded but session cookie missing")

        self.logged_in = True
        return True

    # -------------------------
    # SESSION GUARANTEE
    # -------------------------
    def ensure_login(self):
        if not self.logged_in:
            self.login()

    # -------------------------
    # GENERIC REQUEST WRAPPER
    # -------------------------
    def request(self, method: str, path: str, **kwargs):
        self.ensure_login()

        url = f"{self.base_url}{path}"
        resp = self.session.request(method, url, verify=False, **kwargs)

        # auto-recover session expiry
        if resp.status_code == 401:
            self.logged_in = False
            self.login()
            resp = self.session.request(method, url, verify=False, **kwargs)

        return resp

    # -------------------------
    # HELPERS
    # -------------------------
    def get_user(self):
        return self.request("GET", "/user").json()

    def get_schedules(self):
        return self.request("GET", "/schedules")
