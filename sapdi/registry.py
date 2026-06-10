from sapdi.tools.user import get_user
from sapdi.tools.schedules import get_schedules
from sapdi.tools.health import health_check


def bind_tools(mcp, context):
    """
    MCP Tool Factory:
    binds all tools with shared SAP DI context
    """

    @mcp.tool()
    def tool_get_user():
        return get_user(context)

    @mcp.tool()
    def tool_get_schedules():
        return get_schedules(context)

    @mcp.tool()
    def tool_health():
        return health_check(context)
