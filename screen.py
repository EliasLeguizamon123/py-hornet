import curses
from curses import wrapper

def mainScreen():
    #Call screen
    curses.wrapper(printScreen)

def printScreen(screen):
    # Print text in screen and close when press key
    screen.addstr('Press a key to close the program...')  
    screen.refresh()
    screen.getch()