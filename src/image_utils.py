from typing import Tuple


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
