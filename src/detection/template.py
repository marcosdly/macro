from cv2.typing import MatLike
import cv2 as cv
import numpy as np
from src.image_utils import Rectangle
from typing import List


def template_detect(frame: MatLike, to_detect: MatLike) -> List[Rectangle]:
  detect_gray = cv.cvtColor(to_detect, cv.COLOR_BGR2GRAY)
  frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  h, w = to_detect.shape[:-1]
  result = cv.matchTemplate(frame_gray, detect_gray, cv.TM_CCOEFF_NORMED)
  thresh = 0.8
  regions = np.where(result >= thresh)
  rects = []
  for pt in zip(*regions[::-1]):
    rects.append(Rectangle(pt, (pt[0] + w, pt[1] + h)))
  return rects
