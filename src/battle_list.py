from typing import List
import numpy as np
from src.detection.template import template_detect
from src.detection.text import find_text
from src.image_utils import Rectangle, draw_x_inplace, Color
from cv2.typing import MatLike, Scalar
from datetime import datetime, timedelta
from pynput.mouse import Controller, Button
from base64 import b64encode
import eel
import cv2 as cv
from enum import StrEnum, auto


class EnemyDisplayState(StrEnum):
  ENEMY = auto()
  NOTHING = auto()


class BattleList:
  def __init__(self):
    self.last_action_time = datetime.now()
    self.mouse = Controller()
    self.clicked_once = False
    self.confirmed_target_once = False
    self.last_enemy_display_state = EnemyDisplayState.NOTHING

  def calculate_from(self, frame: MatLike, *, calc_win_title_pos: bool = False):
    self.frame = frame
    if calc_win_title_pos or getattr(self, "window_title", None) is None:
      self.window_title = self._window_title()
    self.topmost_enemy = self._topmost_enemy()

    x, y = self.topmost_enemy.top_left
    self.enemy_target_region = Rectangle(
      (x, y), (x + 30, y + self.topmost_enemy.height)
    )

    self.clicked_once = False
    self.confirmed_target_once = False

  def display_enemy(self, current: EnemyDisplayState, *, force=False):
    if self.last_enemy_display_state == current and not force:
      return

    x1, y1 = self.topmost_enemy.top_left
    x2, y2 = self.topmost_enemy.bottom_right
    enemy_frame = self.frame[y1:y2, x1:x2]
    enemy_frame = cv.cvtColor(enemy_frame, cv.COLOR_BGR2RGB)
    ok, enemy_buffer = cv.imencode(".png", enemy_frame)

    if ok:
      b64 = b64encode(enemy_buffer)
      eel.setEnemyImage(b64.decode())
    else:
      eel.setEnemyImage("")

    self.last_enemy_display_state = current

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

  def _has_color_frame_around(self, color: Scalar) -> bool:
    if not self.enemy_target_region:
      return False

    x1, y1 = self.enemy_target_region.top_left
    x2, y2 = self.enemy_target_region.bottom_right
    subimage = self.frame[y1:y2, x1:x2]
    h = subimage.shape[0]

    row = subimage[h // 2]  # center
    specific_pixel = row[4]
    threshold = Color(*color)
    px_color = Color(*specific_pixel)
    if (
      px_color.red >= threshold.red
      and px_color.green < threshold.green
      and px_color.blue < threshold.blue
    ):
      return True
    return False

  def draw_around(self):
    self.window_title.draw_over(self.frame)
    self.topmost_enemy.draw_over(self.frame)
    self.enemy_target_region.draw_over(self.frame)

    draw_x_inplace(
      self.frame,
      self.topmost_enemy.center,
      line_length_px=self.topmost_enemy.height,
      color=(0, 255, 255),
      thickness=2,
    )

  def _click_enemy(self):
    before = self.mouse.position
    self.mouse.position = self.topmost_enemy.center
    self.mouse.press(Button.left)
    eel.sleep(0.1)
    self.mouse.release(Button.left)
    self.mouse.position = before
    self.last_action_time = datetime.now()

  def _has_any_pitch_black(self):
    x1, y1 = self.enemy_target_region.top_left
    x2, y2 = self.enemy_target_region.bottom_right
    region = self.frame[y1:y2, x1:x2]
    reshaped = region.reshape(-1, region.shape[-1])

    for arr in reshaped:
      truth_table = arr < [30, 30, 30]
      if np.all(truth_table):
        return True

    return False

  def try_action(self):
    if datetime.now() - self.last_action_time < timedelta(seconds=2):
      return

    red = (130, 50, 50)
    if self._has_color_frame_around(red):
      # already in combat
      if not self.confirmed_target_once:
        self.confirmed_target_once = True
      return

    if not self._has_any_pitch_black():
      # nothing on screen
      self.display_enemy(EnemyDisplayState.NOTHING)
      return

    if self.clicked_once and self.confirmed_target_once:
      return

    self.display_enemy(EnemyDisplayState.ENEMY, force=True)
    self._click_enemy()
    self.clicked_once = True
