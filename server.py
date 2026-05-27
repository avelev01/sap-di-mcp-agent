from fastmcp import FastMCP
from sapdi.client import list_graphs, run_graph, get_logs

mcp = FastMCP("SAP-DI-Agent")

# -------------------------
# TOOL: List graphs
# -------------------------
@mcp.tool()
def list_di_graphs():
    """List all SAP DI graphs"""
    return list_graphs()


# -------------------------
# TOOL: Run graph
# -------------------------
@mcp.tool()
def execute_graph(graph_id: str):
    """Run a SAP DI graph by ID"""
    return run_graph(graph_id)


# -------------------------
# TOOL: Get logs
# -------------------------
@mcp.tool()
def graph_logs(graph_id: str):
    """Fetch logs for a graph"""
    return get_logs(graph_id)


if __name__ == "__main__":
    mcp.run()
