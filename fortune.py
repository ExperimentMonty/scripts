#! /usr/bin/env python3
# Reads in fortunes from fortune.txt.  More fortunes always welcome!
# Please observe the following STANDARDS to keep all 'fortunes' looking nice
# and clean.

from random import choice
from textwrap import wrap
from argparse import ArgumentParser

parser = ArgumentParser(description="Print a quote from fortune.txt")
parser.add_argument('-n', '--no-wrap', action='store_true',
                    help="don't use curses and fancy line wrapping")
args = parser.parse_args()

if not args.no_wrap:
    import curses
    stdscr = curses.initscr()
    maxy, maxx = stdscr.getmaxyx()
    curses.endwin()

f = open("scripts/fortune.txt", "r")

raw = f.readlines()

fortunes = []
temp_string = ''
for line in raw:
    if line == '\n':
        fortunes.append(temp_string)
        temp_string = ''
    else:
        if args.no_wrap:
            temp_string += line
        else:
            temp_string += '\n'.join(wrap(line, maxx)) + '\n'

print(choice(fortunes))
