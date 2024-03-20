import os.path as path
from src.eventloop import eventloop

if __name__ == "__main__":
    footage = path.expanduser("~/Videos/tibia-example-footage.mkv")
    eventloop(footage)