from cv2.typing import MatLike
import cv2 as cv
from typing import cast
import numpy as np

def template_detect(frame: MatLike, to_detect: MatLike):
    detect_gray = cv.cvtColor(to_detect, cv.COLOR_BGR2GRAY)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    h, w = to_detect.shape[:-1]
    result = cv.matchTemplate(frame_gray, detect_gray, cv.TM_CCOEFF_NORMED)
    thresh = .8
    regions = np.where(result >= thresh)
    new_frame = frame.copy()
    for pt in zip(*regions[::-1]):
        cv.rectangle(new_frame, pt, (pt[0] + w, pt[1] + h), 255, 2)
    return new_frame, regions, (w, h)