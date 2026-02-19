from mcp_schrodinger.server import mcp


def main():
    mcp.run(transport="stdio")
