from sapdi.context import MCPContext

CONFIG = {
    "BASE_URL": "https://vsystem.ingress....",
    "TENANT": "default",
    "USERNAME": "diadmin",
    "PASSWORD": "*****"
}

# 👇 THIS is the injection point
context = MCPContext(CONFIG)
