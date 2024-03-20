# from src.input.basic import click
from src.battle_list import BattleList
import cv2 as cv
# from datetime import datetime, timedelta


def eventloop(cap_source: int | str) -> None:
  cap = cv.VideoCapture(cap_source)
  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
  cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
  cap.set(cv.CAP_PROP_FPS, 60)
  window_name = "Visualization"
  cv.namedWindow(window_name, cv.WINDOW_GUI_NORMAL)
  battle_list = BattleList()
  while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
      break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    battle_list.calculate_from(frame)
    battle_list.draw_around()
    battle_list.try_action()

    cv.imshow(window_name, cv.cvtColor(frame, cv.COLOR_RGB2BGR))
    if cv.waitKey(1) == ord("q"):
      cv.destroyWindow(window_name)
      break

  cap.release()
