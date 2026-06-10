def get_schedules(context: MCPContext):
    """
    MCP Tool: fetch DI schedules
    """
    resp = context.sapdi.request("GET", "/schedules")

    if resp.status_code == 404:
        return {"error": "Schedules API not available"}

    return resp.json()
