import curses

stdscr = curses.initscr()
curses.noecho() # hide key inputs
curses.cbreak() # make it respond to input immediately