from typing import Tuple
from cv2.typing import MatLike, Scalar
import cv2 as cv


class Rectangle:
  def __init__(self, top_left: Tuple[int, int], bottom_right: Tuple[int, int]):
    self.top_left = top_left
    self.bottom_right = bottom_right

  @property
  def both_ends(self):
    return (self.top_left, self.bottom_right)

  @property
  def width(self):
    return self.bottom_right[0] - self.top_left[0]

  @property
  def height(self):
    return self.bottom_right[1] - self.top_left[1]

  @property
  def size(self):
    return (self.width, self.height)

  @property
  def center(self):
    pt = self.top_left
    return (pt[0] + self.width // 2, pt[1] + self.height // 2)

  def draw_over(
    self, frame: MatLike, color: Scalar = (254, 0, 0), thickness: int = 2
  ):
    cv.rectangle(frame, *self.both_ends, color, thickness)
