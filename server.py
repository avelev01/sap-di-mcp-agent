from mcp import MCPServer
from sapdi.context import MCPContext
from sapdi.registry import bind_tools

server = MCPServer()

context = MCPContext()

bind_tools(server, context)

server.run()
