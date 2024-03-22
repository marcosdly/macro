import eel
import json
from src.client.common import config_path
import cv2 as cv
from capture_devices import devices
import win32com.client


@eel.expose
def getOBSInputOptions() -> str:
  found = devices.run_with_param(device_type="video", list_all=True, result_=True)
  if not found:
    return json.dumps([])

  def parse_once(device_name_string: str) -> str:
    return device_name_string.strip().split(":")[1].strip()

  if isinstance(found, str):
    return json.dumps([{"index": 0, "title": parse_once(found)}])

  devs = [
    {"index": i, "title": parse_once(dev_name_str)}
    for i, dev_name_str in enumerate(found)
  ]

  return json.dumps(devs)


@eel.expose
def setOBSInputOptions(title: str, index: int) -> None:
  with open(config_path, "r") as file:
    config = json.load(file)

  config["obsinput"] = {"index": index, "title": title}

  with open(config_path, "w") as file:
    json.dump(config, file)
