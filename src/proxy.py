import requests
import uvicorn

from mcp.server.fastmcp import FastMCP

from starlette.applications import Starlette
from starlette.routing import Mount


mcp = mcp = FastMCP("Raspberry Pi Relay Toggle MCP Server")


@mcp.tool()
def activate(duration: int = 1, host: str = "192.168.0.214", port: int = 5000) -> dict:
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


app = Starlette(
  routes=[
    Mount("/", app=mcp.sse_app()),
  ]
)


def main():
  uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
  main()
