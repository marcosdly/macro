from dataclasses import dataclass


@dataclass(init=False)
class State:
  running: bool = False
  visualize: bool = False
