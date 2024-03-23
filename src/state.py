from dataclasses import dataclass
from src.client.common import config_path
import json


@dataclass(init=True)
class _StateType:
  running: bool = False
  visualize: bool = False
  __json_state: dict | None = None

  @property
  def persistent(self) -> dict:
    if self.__json_state:
      return self.__json_state

    with open(config_path) as file:
      self.__json_state = json.load(file)

    return self.__json_state


State = _StateType()
