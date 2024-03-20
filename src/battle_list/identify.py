from src.detection.template import template_detect
from src.detection.threshold import in_color_range
from src.detection.text import find_text
from src.image_utils import Rectangle
from cv2.typing import MatLike
import cv2 as cv


def find_window(frame: MatLike) -> Rectangle:
  to_detect = cv.imread("assets/battle_list/window_title.png")
  rectangles = template_detect(frame, to_detect)
  return rectangles[0]


def topmost_enemy_region(initial: Rectangle) -> Rectangle:
  factor = 1.5
  top_left = (initial.top_left[0], initial.top_left[1] + initial.height)
  bottom_right = (
    int(top_left[0] + (initial.width * factor)),
    int(top_left[1] + (initial.height * factor)),
  )
  return Rectangle(top_left, bottom_right)


def enemy_target_contour(frame: MatLike, enemy_region: Rectangle) -> Rectangle | None:
  red = (255, 0, 0)
  black = (254, 0, 0)
  x1, y1 = enemy_region.top_left
  x2, y2 = enemy_region.bottom_right
  enemy_image_slice = frame[y1:y2, x1:x2]
  threshold_rectangles = in_color_range(enemy_image_slice, black, red)

  if len(threshold_rectangles) == 0:
    return None

  relevant_rect = threshold_rectangles[0]
  top_left = (x1 + relevant_rect.top_left[0], y1 + relevant_rect.top_left[1])
  bottom_right = (top_left[0] + relevant_rect.width, top_left[1] + relevant_rect.height)

  return Rectangle(top_left, bottom_right)


def text_exist_in_enemy_region(frame: MatLike, enemy_region: Rectangle):
  x1, y1 = enemy_region.top_left
  x2, y2 = enemy_region.bottom_right
  h, w = frame.shape[:-1]
  enemy_image_slice = frame[y1:y2, x1:x2]
  rects, texts = find_text(enemy_image_slice)
  normalized_rects = []
  for rectangle in rects:
    x, y = rectangle.top_left
    normalized_rects.append(
      Rectangle((x1 + x, y1 + y), (x1 + x + rectangle.width, y1 + y + rectangle.height))
    )
  return normalized_rects, texts
