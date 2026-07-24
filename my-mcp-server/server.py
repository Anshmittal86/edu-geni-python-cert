# uv add mcp[cli]
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP('calculator')

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add a and b"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply a and b"""
    return a * b

@mcp.tool()
def division(a: float, b: float) -> float:
    """Divide a by b"""
    return a / b

if __name__ == "__main__":
    mcp.run(transport="stdio")
