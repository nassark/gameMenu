import curses
import time

#.initscr() initializes a window object, in this case the stdscr is the window
#object of this program
stdscr = curses.initscr()

Menu = ['Home', 'Play', 'Scoreboard', 'Exit']

#This function will print the menu to the window terminal.
def print_menu(stdscr, selectedRowId):
	stdscr.clear()
	#.getmaxyx() returns the width and height of window as tuple (y,x)
	h,w = stdscr.getmaxyx()
	for idx, row in enumerate(Menu):
		x = w//2 - len(row)//2
		y = h//2 - len(Menu)//2 + idx
		if idx == selectedRowId:
			#.attron will activate the color pair
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y,x, row)
			#.attroff will deactivate the color pair
			stdscr.attroff(curses.color_pair(1))
		else:
			#.addstr() allows us to print string to window object
			stdscr.addstr(y,x, row)

	stdscr.refresh()


#This main function will act as the driver code to the menu program
def main(stdscr):
	#.init_pair will initialize a color pair
	curses.init_pair(1, curses.COLOR_BLACK,curses.COLOR_WHITE)
	currentRowID = 0
	curses.curs_set(0)
	print_menu(stdscr, currentRowID)

	while (True):
		key = stdscr.getch()
		stdscr.clear()

		# The first IF statement will decrement the currentRowID to the previous Menu item
		if key == curses.KEY_UP and currentRowID > 0:
			currentRowID -= 1
		#The first ELIF statement will increment the currentRowID to the next Menu item
		elif key == curses.KEY_DOWN and currentRowID < len(Menu) - 1:
			currentRowID += 1
		elif key == curses.KEY_ENTER or key in [10,13]:
			stdscr.addstr(0,0, "You pressed {}".format(Menu[currentRowID]))
			stdscr.refresh()
			stdscr.getch()
			if currentRowID == len(Menu) - 1:
				break

		print_menu(stdscr, currentRowID)
		stdscr.refresh()


curses.wrapper(main)
