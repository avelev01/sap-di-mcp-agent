def get_user(context):
    """
    MCP Tool: returns logged-in SAP DI user info
    """
    response = context.sapdi.request("GET", "/user")
    return response.json()
