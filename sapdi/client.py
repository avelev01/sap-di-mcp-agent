import requests


class SAPDIClient:
    def __init__(self, base_url, tenant, username, password):
        self.base_url = base_url.rstrip("/")
        self.password = password
        self.tenant = tenant
        self.username = username
        

        self.session = requests.Session()
        self.logged_in = False

    # bootstrap cookies
    def _bootstrap(self):
        self.session.get(
            f"{self.base_url}/login/?tenant={self.tenant}",
            verify=False
        )

    # login
    def login(self):
        self._bootstrap()

        resp = self.session.post(
            f"{self.base_url}/api/login/v2/finalize",
            json={
                "tenant": self.tenant,
                "username": self.username,
                "password": self.password
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

        if "vsystem-session-id" not in self.session.cookies:
            raise Exception("No session cookie received")

        self.logged_in = True

    # safe request wrapper
    def request(self, method, path, **kwargs):
        if not self.logged_in:
            self.login()

        url = f"{self.base_url}{path}"
        resp = self.session.request(method, url, verify=False, **kwargs)

        # auto-relogin
        if resp.status_code == 401:
            self.logged_in = False
            self.login()
            resp = self.session.request(method, url, verify=False, **kwargs)

        return resp
