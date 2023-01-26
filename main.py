import curses
import curses.ascii
from args import generateArgs
from book import readEpub, getContent
import os
from time import sleep
    
def mainScreen(screen):
    output = generateArgs()
    columns = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    pages = []
    y = 1
    x = 0
    for chapters in output:
        for character in chapters:
            if y < rows - 3:
                if x < columns:
                    screen.addstr(y, x, character)
                    sleep(0.0001)
                    screen.refresh()
                    x += 1
                else :
                    y += 1
                    x = 0
            else:
                key = screen.getch()
                screen.clear()
                y = 1
                continue         
        
    # while 1:
    # key = screen.getch()
    #     screen.clear()
    #     if key == curses.KEY_UP:
    #         screen.addstr(0, 0, "You pressed Up key!")
    #     elif key == curses.KEY_DOWN:
    #         screen.addstr(0, 0, "You pressed Down key!")
    #     elif key == curses.KEY_ENTER or key in [10, 13]:
    #         screen.addstr(0, 0, "You pressed Enter.")
    #     elif key == curses.ascii.ESC or ord('q'):
    #         return


if __name__ == "__main__":
  curses.wrapper(mainScreen)