# uv add mcp[cli]
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP('my-server')

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add a and b"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Add a and b"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Add a and b"""
    return a * b

@mcp.tool()
def division(a: float, b: float) -> float:
    """Add a and b"""
    return a / b

if __name__ == "__main__":
    mcp.run()
