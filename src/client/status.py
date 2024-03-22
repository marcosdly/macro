import eel
from src.state import State


@eel.expose
def setRunningState(state: bool) -> bool:
  if not isinstance(state, bool):
    return False
  State.running = state
  return True


@eel.expose
def setVisualizeState(state: bool) -> bool:
  if not isinstance(state, bool):
    return False
  State.visualize = state
  return True
