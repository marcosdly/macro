from src.battle_list.identify import (
  find_window,
  topmost_enemy_region,
  enemy_target_contour,
  text_exist_in_enemy_region,
)
import cv2 as cv


def eventloop(cap_source: int | str) -> None:
  cap = cv.VideoCapture(cap_source)
  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
  cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
  cap.set(cv.CAP_PROP_FPS, 30)
  while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
      break
    window_title = find_window(frame)
    first_enemy_region = topmost_enemy_region(window_title)
    enemy_contour = enemy_target_contour(frame, first_enemy_region)
    text_regions, texts = text_exist_in_enemy_region(frame, first_enemy_region)

    cv.rectangle(frame, *window_title.both_ends, 255, 2)
    cv.rectangle(frame, *first_enemy_region.both_ends, 255, 2)
    if enemy_contour:
      cv.rectangle(frame, *enemy_contour.both_ends, 255, 2)
    if len(texts):
      for region in text_regions:
        cv.rectangle(frame, *region.both_ends, (0, 0, 255), 1, cv.LINE_4)

    cv.imshow("Visualization", frame)
    if cv.waitKey(1) == ord("q"):
      cv.destroyAllWindows()
      break

  cap.release()
