from src.client import init, expose_all
from src.eventloop import eventloop
from src.state import State
from src.client.common import config_path
import json
import eel


def main():
  init()
  eel.init("web_client/dist", allowed_extensions=[".js"])
  expose_all()
  eel.start("index.html", block=False, port=9997, size=(800, 600))

  while True:
    eel.sleep(1)

    if not State.running:
      continue

    with open(config_path) as file:
      obj = json.load(file)

    obs_input = obj["obsinput"]
    if obs_input is None:
      continue

    obs_index = obs_input["index"]
    if obs_index is None:
      continue

    eventloop(obs_index)
    eel.toggleUIRunningState()


if __name__ == "__main__":
  main()
