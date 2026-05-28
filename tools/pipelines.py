from sapdi.session_manager import get_sap_session


def list_pipelines():
    """
    MCP Tool: Fetch SAP DI pipelines
    """
    sap = get_sap_session()
    return sap.get("/app/pipeline-modeler/service/v1/pipelines")