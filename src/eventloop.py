from src.battle_list.identify import (
  find_window,
  topmost_enemy_region,
  text_exist_in_enemy_region,
)
from src.image_utils import draw_x_inplace
import cv2 as cv


def eventloop(cap_source: int | str) -> None:
  cap = cv.VideoCapture(cap_source)
  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
  cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
  cap.set(cv.CAP_PROP_FPS, 30)
  window_name = "Visualization"
  cv.namedWindow(window_name, cv.WINDOW_GUI_NORMAL)
  while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
      break
    window_title = find_window(frame)
    first_enemy_region = topmost_enemy_region(window_title)
    text_regions, texts = text_exist_in_enemy_region(frame, first_enemy_region)

    window_title.draw_over(frame)
    first_enemy_region.draw_over(frame)
    if len(texts):
      for region in text_regions:
        region.draw_over(frame, color=(0, 255, 0), thickness=1)

    draw_x_inplace(
      frame, first_enemy_region.center, line_length_px=first_enemy_region.height
    )

    cv.imshow(window_name, frame)
    if cv.waitKey(1) == ord("q"):
      cv.destroyWindow(window_name)
      break

  cap.release()
