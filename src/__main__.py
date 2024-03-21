import eel


def main():
  eel.init("web_client/dist")
  eel.start("index.html", block=True)


if __name__ == "__main__":
  main()
