from src.battle_list import BattleList
import cv2 as cv
from src.state import State
import eel


def eventloop(cap_source: int | str) -> None:
  fps = 30
  cap = cv.VideoCapture(cap_source)
  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
  cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
  cap.set(cv.CAP_PROP_FPS, fps)

  window_name = "Visualization"
  if State.visualize:
    cv.namedWindow(window_name, cv.WINDOW_GUI_NORMAL)

  battle_list = BattleList()
  counter = 0

  while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
      break
    counter += 1
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    try:
      battle_list.calculate_from(frame, calc_win_title_pos=counter % fps == 0)
      battle_list.try_action()
    except:
      cv.destroyAllWindows()
      break

    if State.visualize:
      battle_list.draw_around()
      cv.imshow(window_name, cv.cvtColor(frame, cv.COLOR_RGB2BGR))
      cv.waitKey(1)

    if not State.running:
      cv.destroyAllWindows()
      break

    eel.sleep(0.3)

  cap.release()
