from src.state import State


def setRunningState(state: bool) -> bool:
  if not isinstance(state, bool):
    return False
  State.running = state
  return True


def setVisualizeState(state: bool) -> bool:
  if not isinstance(state, bool):
    return False
  State.visualize = state
  return True
