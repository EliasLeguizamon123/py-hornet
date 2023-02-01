import curses, os, curses.ascii
from time import sleep
from book import createPages
from args import generateArgs
    
def mainScreen(screen):
    #default conf
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()
    #default vars
    output = generateArgs()
    pages = createPages(output, size=[curses.LINES - 1, curses.COLS - 1])
    x = 2
    y = 2
    #default win
    win = curses.newwin(curses.LINES, curses.COLS)
    win.keypad(True)
    index = 0
    
    while True: 
        page = pages[index]
        win.box()
        for word in page.split() :
            if y <= curses.LINES - 3 :
                if x + len(word) > curses.COLS - 2:
                    y += 1
                    x = 2

                win.addstr(y, x, word)
                win.addstr(y, x - 1, ' ')
                sleep(0.0001)
                win.refresh()
                x += len(word) + 1
            
            else :
                y = 2
                x = 2
                win.addstr(y, x, word)
                win.addstr(y, x - 1, ' ')
                sleep(0.0001)
                x += len(word) + 1
                win.clear()
        y = 2
        x = 2
        win.refresh()
        key = win.getch()
        win.clear()
        
        if key == curses.KEY_UP:
            if index < 1:
                index = 0
            else :
                index = index - 1
        if key == curses.KEY_DOWN and index >= 1:
            index = index + 1
            


if __name__ == "__main__":
    curses.wrapper(mainScreen)
    # mainScreen()