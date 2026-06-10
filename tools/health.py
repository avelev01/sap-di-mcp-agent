def health_check(context):
    resp = context.sapdi.request("GET", "/user")

    return {
        "status": resp.status_code,
        "authenticated": resp.status_code == 200
    }
