from cv2.typing import MatLike
import pytesseract
from typing import Tuple, List
from src.image_utils import Rectangle

pytesseract.pytesseract.tesseract_cmd = (
  r"C:\Users\gabas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)


def find_text(frame: MatLike) -> Tuple[List[Rectangle], List[str]]:
  data = pytesseract.image_to_data(frame, "eng", output_type=pytesseract.Output.DICT)
  indexes = [(i, txt) for i, txt in enumerate(data["text"]) if txt.strip()]
  rects = []
  texts = []
  for i, txt in indexes:
    x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
    rects.append(Rectangle((x, y), (x + w, y + h)))
    texts.append(txt)
  return rects, texts
