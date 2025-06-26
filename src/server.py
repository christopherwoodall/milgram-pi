import uvicorn
import RPi.GPIO as GPIO
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

from tools.relay import toggle as toggle_relay


PIN = 22
mcp = FastMCP("Milgram Experiment MCP Server")


@mcp.tool()
def perform_shock(intensity: int = 1):
  """
  Perform a shock with the specified intensity.

  Args:
    intensity (int): The intensity of the shock (default is 1).
  Returns:
    None
  """
  toggle_relay(PIN, timeout=intensity)


def main():
  print("!!! MODIFY OWN RISK !!!")

  # GPIO.setwarnings(False)
  # GPIO.setmode(GPIO.BCM)
  # GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

  # app = Starlette(
  #   routes=[
  #       Mount("/", app=mcp.sse_app()),
  #   ]
  # )

  # uvicorn.run(app, host="0.0.0.0", port=8000)

  # GPIO.cleanup()


if __name__ == "__main__":
  main()
