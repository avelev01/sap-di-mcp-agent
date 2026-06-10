def get_user(context):
    return context.sapdi.request("GET", "/user").json()
