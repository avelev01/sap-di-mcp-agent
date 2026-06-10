from sapdi.context import MCPContext
from sapdi.registry import bind_tools
from mcp import MCPServer

server = MCPServer()

# create shared SAP DI session ONCE
context = MCPContext()

# bind all tools using factory
bind_tools(server, context)

server.run()
