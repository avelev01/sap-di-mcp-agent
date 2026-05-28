from sapdi.session_manager import get_sap_session


def list_graphs():
    """
    MCP Tool: List all SAP DI graphs
    """
    sap = get_sap_session()

    return sap.get(
        "/app/pipeline-modeler/service/v1/repository/graphs"
    )


def run_graph(graph_id: str):
    """
    MCP Tool: Run a SAP DI graph
    """
    sap = get_sap_session()

    return sap.session.post(
        f"{sap.base_url}/app/pipeline-modeler/service/v1/runtime/graphs/{graph_id}/run",
        verify=False
    ).json()


def get_graph_logs(graph_id: str):
    """
    MCP Tool: Get execution logs of a graph
    """
    sap = get_sap_session()

    return sap.get(
        f"/app/pipeline-modeler/service/v1/logs/{graph_id}"
    )
