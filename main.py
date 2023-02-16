import curses, curses.ascii

from time import sleep
from book import createPages
from args import generateArgs
from savingData import saveNewBookInData, saveActualState
    
def mainScreen(screen):
    #default conf
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()
    #default vars
    output = generateArgs()
    pages = createPages(output["content"], size=[curses.LINES - 1, curses.COLS - 1])
    x = 2
    y = 2
    #default win
    win = curses.newwin(curses.LINES, curses.COLS)
    win.keypad(True)
    index = 0
    saveNewBookInData({"bookPath": output['bookPath'], "bookTitle": output['bookTitle'], "actualPage": index, "pagesLength": len(pages)})
    
    while True: 
        page = pages[index]
        win.box()
        
        for line in page :
            win.addstr(y, x, line)
            sleep(0.0001)
            win.refresh()
            y += 1
            
        y = 2
        x = 2
        win.refresh()
        key = win.getch()
        win.clear()
        
        if key == curses.KEY_UP :
            if index < 1:
                index = 0
            else :
                index = index - 1
        if key == curses.KEY_DOWN :
            index = index + 1
        if key == ord('q') : 
            saveActualState({"bookPath": output['bookPath'], 'bookTitle': output['bookTitle'], "actualPage": index, 'pagesLength': len(pages)})
            break


if __name__ == "__main__":
    curses.wrapper(mainScreen)
