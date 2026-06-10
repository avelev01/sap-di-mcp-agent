def get_schedules(context):
    """
    MCP Tool: returns schedules from SAP DI
    """
    response = context.sapdi.request("GET", "/schedules")
    
    if response.status_code == 404:
        return {"error": "Endpoint not available in this tenant"}

    return response.json()
