from src.client.common import config_path, config_dir
from src.client.configuration import (
  getOBSInputOptions,
  setOBSInputOptions,
  getOBSConfig,
)
from src.client.status import (
  setRunningState,
  setVisualizeState,
  getRunningState,
  getVisualizeState,
)
import os
import eel


def init() -> None:
  if not os.path.isdir(config_dir):
    os.makedirs(config_dir, exist_ok=True)

  if not os.path.isfile(config_path):
    with open(config_path, "wt") as file:
      file.write("{}")


def expose_all() -> None:
  [
    eel.expose(func)
    for func in [
      getOBSInputOptions,
      setOBSInputOptions,
      getOBSConfig,
      setVisualizeState,
      setRunningState,
      getVisualizeState,
      getRunningState,
    ]
  ]
