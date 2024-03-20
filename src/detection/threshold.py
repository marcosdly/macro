from src.image_utils import Rectangle
from typing import List
from cv2.typing import MatLike, Scalar
import cv2 as cv


def in_color_range(
  frame: MatLike, lowerbound: Scalar, upperbound: Scalar
) -> List[Rectangle]:
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  threshold = cv.inRange(hsv, lowerbound, upperbound)
  contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  rects = []
  for cont in contours:
    x, y, w, h = cv.boundingRect(cont)
    rects.append(Rectangle((x, y), (x + w, y + h)))
  return rects
