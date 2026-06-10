def check_di_health(context):
    """
    MCP Tool: verifies SAP DI session is alive
    """
    resp = context.sapdi.request("GET", "/user")

    return {
        "status": resp.status_code,
        "authenticated": resp.status_code == 200,
        "user": resp.json() if resp.status_code == 200 else None
    }
