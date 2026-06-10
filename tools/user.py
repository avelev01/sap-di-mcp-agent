def get_user(context: MCPContext):
    """
    MCP Tool: returns SAP DI user info
    """
    resp = context.sapdi.request("GET", "/user")
    return resp.json()
