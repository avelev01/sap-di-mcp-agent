import os
import requests
from dotenv import load_dotenv

load_dotenv()

SAP_DI_URL = os.getenv("SAP_DI_URL")
TOKEN = os.getenv("SAP_DI_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def list_graphs():
    url = f"{SAP_DI_URL}/app/pipeline-modeler/service/v1/repository/graphs"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()


def run_graph(graph_id: str):
    url = f"{SAP_DI_URL}/app/pipeline-modeler/service/v1/runtime/graphs/{graph_id}/run"
    r = requests.post(url, headers=headers)
    r.raise_for_status()
    return r.json()


def get_logs(graph_id: str):
    url = f"{SAP_DI_URL}/app/pipeline-modeler/service/v1/logs/{graph_id}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()
