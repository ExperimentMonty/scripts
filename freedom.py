#! /usr/bin/env python3
# With major kudos to Tobit for inspiring a more interesting
# opening shell script

import curses

stdscr = curses.initscr()
maxy, maxx = stdscr.getmaxyx()
curses.endwin()

printblue = '\033[44m\033[37m'
printred = '\033[41m\033[37m'
printwhite = '\033[47m'
resetprint = '\033[0m'

line1 = printblue + ' * * * * * * * * ' + printred + ' ' * 30 + resetprint
line2 = printblue + '  * * * * * * *  ' + printwhite + ' ' * 30 + resetprint
line3 = printwhite + ' ' * 47 + resetprint
line4 = printred + ' ' * 47 + resetprint
space = ' ' * int((maxx - 47)/2)

print(space+line1)
print(space+line2)
print(space+line1)
print(space+line2)
print(space+line1)
print(space+line2)
print(space+line1)
print(space+line3)
print(space+line4)
print(space+line3)
print(space+line4)
print(space+line3)
print(space+line4)
print(resetprint)
