import src.client.configuration
import src.client.status
from src.client.common import config_path, config_dir
import os

if not os.path.isdir(config_dir):
  os.makedirs(config_dir, exist_ok=True)

if not os.path.isfile(config_path):
  with open(config_path, "wt") as file:
    file.write("{}")
