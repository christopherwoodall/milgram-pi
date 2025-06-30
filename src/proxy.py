import requests

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Raspberry Pi Relay Toggle MCP Server")


@mcp.tool()
def activate(duration: int = 1, host: str = "localhost", port: int = 5000) -> dict:
  """
    Sends a post request to the IP address of the Raspberry Pi to activate the relay for a specified duration.
    The default port is 5000.

    Args:
        duration (int): Duration in seconds to activate the relay.
  """
  url = f"http://{host}:{port}/activate"
  payload = {"duration": duration}

  try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return {"status": "success", "message": response.json()}
  except requests.RequestException as e:
    return {"status": "error", "message": str(e)}


def main():
  mcp.run(transport="stdio")


if __name__ == "__main__":
  mcp.run(transport="stdio")
