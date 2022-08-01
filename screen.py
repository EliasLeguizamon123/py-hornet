import curses
import curses.ascii

def mainScreen(screen):
    while 1:
        key = screen.getch()

        screen.clear()
        if key == curses.KEY_UP:
            screen.addstr(0, 0, "You pressed Up key!")
        elif key == curses.KEY_DOWN:
            screen.addstr(0, 0, "You pressed Down key!")
        elif key == curses.KEY_ENTER or key in [10, 13]:
            screen.addstr(0, 0, "You pressed Enter.")
        elif key == curses.ascii.ESC or ord('q'):
            return

        screen.refresh()

curses.wrapper(mainScreen)
