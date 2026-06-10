def get_schedules(context):
    resp = context.sapdi.request("GET", "/schedules")

    if resp.status_code == 404:
        return {"error": "schedules not available"}

    return resp.json()
