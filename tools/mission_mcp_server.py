"""SpaceRescue MCP server."""

from mcp.server.fastmcp import FastMCP

from tools.mission_tools import (
    get_high_priority_missions,
    get_mission_status,
    list_all_missions,
)

server = FastMCP("SpaceRescue Mission Tools")


@server.tool()
def mission_status(mission_id: int) -> dict:
    """Get the status of a mission by ID."""
    return get_mission_status(mission_id)


@server.tool()
def list_missions() -> list:
    """List all SpaceRescue missions."""
    return list_all_missions()


@server.tool()
def high_priority_missions() -> list:
    """List active high-priority missions."""
    return get_high_priority_missions()


if __name__ == "__main__":
    server.run()