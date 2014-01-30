#!/usr/bin/python

#This script uses the cliclick application to create a
#simple auto-clicker. The program will do a triple-
#click every <delay> seconds for 60 seconds, then
#move the mouse to the side for <large_delay> seconds
#to give the user a signal and time that this is their
#time to stop the program using Ctrl-C

from time import sleep
from subprocess import call

delay = 0.1
large_delay = 10
i = 0

while True:
    call(['cliclick', 'tc:450,425'])
    sleep(delay)
    i = i + 1
    if i >= (60/delay):
        call(['cliclick', 'tc:0,425'])
        sleep(large_delay)
        i = 0
