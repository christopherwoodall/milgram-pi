import os


def main():
  """
  This is a routing mechanism for `remote.py` and `proxy.py`.
  This script will determine which configuration to run
  based on the environment variable `MILGRAM_MODE`.
  If `MILGRAM_MODE` is set to "remote", it will run the remote server.
  If it is not set or set to any other value, it will run the local server.
  """

  mode = os.getenv("MILGRAM_MODE", "local")

  if mode == "remote":
    import remote
    remote.main()
  else:
    import proxy
    proxy.main()


if __name__ == "__main__":
  main()
