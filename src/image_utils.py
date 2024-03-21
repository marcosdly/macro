from typing import NamedTuple, Tuple
from cv2.typing import MatLike, Scalar
import cv2 as cv


class Rectangle:
  def __init__(self, top_left: Tuple[int, int], bottom_right: Tuple[int, int]):
    self.top_left = top_left
    self.bottom_right = bottom_right
    self.both_ends = (self.top_left, self.bottom_right)
    self.width = self.bottom_right[0] - self.top_left[0]
    self.height = self.bottom_right[1] - self.top_left[1]
    self.size = (self.width, self.height)

    pt = self.top_left
    self.center = (pt[0] + self.width // 2, pt[1] + self.height // 2)

  def draw_over(self, frame: MatLike, color: Scalar = (254, 0, 0), thickness: int = 2):
    cv.rectangle(frame, *self.both_ends, color, thickness)


def draw_x_inplace(
  frame: MatLike,
  center: Tuple[int, int],
  line_length_px: int,
  color: Scalar,
  thickness: int = 2,
):
  center_x, center_y = center
  size = line_length_px // 2
  cv.line(
    frame,
    (center_x - size, center_y - size),
    (center_x + size, center_y + size),
    color,
    thickness,
  )
  cv.line(
    frame,
    (center_x + size, center_y - size),
    (center_x - size, center_y + size),
    color,
    thickness,
  )


class Color(NamedTuple):
  red: int
  green: int
  blue: int
