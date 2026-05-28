import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SAP_DI_BASE_URL = os.getenv(
        "SAP_DI_URL",
        "https://vsystem.ingress.dh-1ts46knm.dhaas-live.shoot.live.k8s-hana.ondemand.com"
    ).rstrip("/")
    SAP_DI_TENANT = os.getenv("SAP_DI_TENANT", "default")
    SAP_DI_USERNAME = os.getenv("SAP_DI_USERNAME", "admin")
    SAP_DI_PASSWORD = os.getenv("SAP_DI_PASSWORD", "Tcccsapcoe2021")
    SAP_DI_API_PREFIX = os.getenv("SAP_DI_API_PREFIX", "/app/pipeline-modeler/service/v1")
    SAP_DI_VERIFY_SSL = os.getenv("SAP_DI_VERIFY_SSL", "true").lower() in ("1", "true", "yes", "on")
    SESSION_CACHE = os.getenv("SAP_DI_SESSION_CACHE", "false").lower() in ("1", "true", "yes", "on")
