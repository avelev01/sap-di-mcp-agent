def get_user(context):
    resp = context.sapdi.request("GET", "/user")
    return resp.json()
