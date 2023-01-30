import curses, os, curses.ascii
from time import sleep
from book import createPages
from args import generateArgs
    
def mainScreen(screen):
    curses.noecho()
    curses.cbreak()
    output = generateArgs()
    size = screen.getmaxyx();
    rows = size[0]
    columns = size[1]
    pages = createPages(output, size)
    x = 1
    y = 1
    index = 0
    page = pages[index]
    win = curses.newwin(curses.LINES, curses.COLS)
    
                 # L    R    T    B   TL   TR   BL   BR
    win.border('{', '}', '~', '~', '+', '+', '+', '+')
    win.refresh()
    win.getch()
    
    # while 1: 

    #     key = screen.getch()
        
    #     for word in page.split():
    #         screen.addstr(y, x, word)
    #         if y <= rows - 3:
    #             if x + len(word) > columns - 1:
    #                 y += 1
    #                 x = 1

    #             screen.addstr(y, x, word)
    #             screen.addstr(y, x - 1, ' ')
    #             sleep(0.0001)
    #             screen.refresh()
    #             x += len(word) + 1
    #         else :
    #             y = 1
    #             x = 1
    #             screen.clear()
    #             screen.addstr(y, x, word)
    #             screen.addstr(y, x - 1, ' ')
    #             sleep(0.0001)
    #             screen.refresh()
    #             x += len(word) + 1
        
    #     if key == curses.KEY_UP:
    #         index += 1
    #     if key == curses.KEY_DOWN and index >= 1:
    #         index -= 1
            


if __name__ == "__main__":
    curses.wrapper(mainScreen)
    # mainScreen()