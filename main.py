from args import generateArgs
# from screen import mainScreen
from book import readEpub, getContent

def main() -> None:
    #Invoke Args, then call book
    generateArgs()
    # mainScreen()

if __name__ == "__main__":
  main()