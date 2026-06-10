def health_check(context: MCPContext):
    """
    MCP Tool: validate SAP DI session
    """
    resp = context.sapdi.request("GET", "/user")

    return {
        "authenticated": resp.status_code == 200,
        "status": resp.status_code
    }
