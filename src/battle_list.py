from typing import List, Tuple
from src.detection.template import template_detect
from src.detection.text import find_text
from src.image_utils import Rectangle, draw_x_inplace
from cv2.typing import MatLike
from datetime import datetime, timedelta
from pynput.mouse import Controller, Button
import time
import cv2 as cv


class BattleList:
  def __init__(self):
    self.last_action_time = datetime.now()
    self.mouse = Controller()

  def calculate_from(self, frame: MatLike):
    self.frame = frame
    self.window_title = self._window_title()
    self.topmost_enemy = self._topmost_enemy()
    self.enemy_name = self._enemy_name()

  def _window_title(self) -> Rectangle:
    to_detect = cv.imread("assets/battle_list/window_title.png")
    rectangles = template_detect(self.frame, to_detect)

    return rectangles[0]

  def _topmost_enemy(self) -> Rectangle:
    factor = 1.5
    top_left = (
      self.window_title.top_left[0],
      self.window_title.top_left[1] + self.window_title.height,
    )
    bottom_right = (
      int(top_left[0] + (self.window_title.width * factor)),
      int(top_left[1] + (self.window_title.height * factor)),
    )

    return Rectangle(top_left, bottom_right)

  def _enemy_name(self):
    x1, y1 = self.topmost_enemy.top_left
    x2, y2 = self.topmost_enemy.bottom_right
    enemy_image_slice = self.frame[y1:y2, x1:x2]
    rects, texts = find_text(enemy_image_slice)
    normalized_rects: List[Rectangle] = []
    for rectangle in rects:
      x, y = rectangle.top_left
      normalized_rects.append(
        Rectangle(
          (x1 + x, y1 + y), (x1 + x + rectangle.width, y1 + y + rectangle.height)
        )
      )

    return normalized_rects, texts

  def draw_around(self):
    self.window_title.draw_over(self.frame)
    self.topmost_enemy.draw_over(self.frame)
    enemy_name_regions, _ = self.enemy_name
    if len(enemy_name_regions):
      for region in enemy_name_regions:
        region.draw_over(self.frame)
    draw_x_inplace(
      self.frame,
      self.topmost_enemy.center,
      line_length_px=self.topmost_enemy.height,
      color=255,
      thickness=1,
    )

  def try_action(self):
    _, texts = self.enemy_name
    if len(texts) == 0 or datetime.now() - self.last_action_time < timedelta(seconds=5):
      return

    before = self.mouse.position
    self.mouse.position = self.topmost_enemy.center
    self.mouse.press(Button.left)
    time.sleep(0.3)
    self.mouse.release(Button.left)
    self.mouse.position = before
    self.last_action_time = datetime.now()
