#!/usr/bin/env python

import random,time,datetime
import curses
import traceback
from baoleidb import DisGroup, DisIP, DisRemotUser

data_vals = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
updt_cnt1 = 0
updt_cnt2 = 0

ran = random.random


def GetDate():
    global currdate
    date = datetime.datetime.now()
    currdate = time.strftime('%Y-%m-%d')

def GetTime():
    global currtime
    time = datetime.datetime.now()
    currtime = time.strftime('%H:%M:%S')

# write data and time to display
def WriteDateTime(win):
    GetDate()
    GetTime()

    win.move(2,15)
    win.clrtoeol()
    win.addstr("%s" % currdate)
    win.move(3,15)
    win.clrtoeol()
    win.addstr("%s" % currtime)
    win.refresh()


# get simulated data input values
def getDataVals():
    pass
    """
    global data_vals, updt_cnt1, updt_cnt2

    data_vals[0] = ran() * 10.0
    data_vals[1] = ran() * 10.0

    if updt_cnt1 >= 4:
        for i in range(2,5):
            data_vals[i] = ran() * 10.0
        updt_cnt1 = 0
    else:
        updt_cnt1 += 1

    if updt_cnt2 >= 10:
        for i in range(4,8):
            data_vals[i] = ran() * 10.0
        updt_cnt2 = 0
    else:
        updt_cnt2 += 1
    """

# write channel data values
def writeDataVals(win):
    pass
    """
    idx = 0
    for i in range(6,14):
        win.move(i,10)
        win.clrtoeol()
        win.addstr("%6.2f" % data_vals[idx])
        idx += 1

    win.refresh()
    # put cursor below display text when update is done
    win.move(16,1)
    """

group_info = {}
ip_info = {}
user_info = {}

# main page
def mainScreen(win):
    win.erase()

    # headline
    win.move(1,30)
    win.addstr("Welcome to use TriAquae TriConn")
    win.refresh()

    # time fence
    win.move(2,1)
    win.addstr("Current Date:")
    win.move(3,1)
    win.addstr("Current Time:")
    win.refresh()
    WriteDateTime(win)

    # content fence
    win.move(6,1)
    win.addstr("  GID\tGroup\t\tExplain\t\tShortcuts")
    gid = 0
    gid_row = 7
    gid_line = 4
    group_row = 7
    group_line = 9
    for g in DisGroup():
        gid = gid + 1
        gid_row = gid_row + 1
        group_row = group_row + 1
        win.addstr(gid_row, gid_line, "%s" % gid)
        win.addstr(group_row, group_line, "%s\n" % g)
        win.refresh()
        group_info = {gid:g}

    # Shortcut bar
    win.move(8,40)
    win.addstr("| [ 1-9 ] choose GID.")
    win.move(9,40)
    win.addstr("| [ q ] quit TriConn.")
    win.refresh()

    #win.move(25,1)
    #win.addstr("Enter X to exit, W for window.")
    #win.refresh()

def chooseIP(win, group_name='BJ'):
    # create a select ip sub-window and keep it open until user presses the X
    #subwin = win.subwin(10, 40, 15, 25)
    subwin = win.subwin(15, 25)
    subwin.nodelay(1)  # disable getch() blocking
    subwin.erase()
    subwin.bkgdset(' ')
    subwin.refresh()

    subwin.addstr(0, 0, "+-----------------------------+")
    subwin.addstr(1, 0, "| ID\tIP                    |")
    id = 0
    row = 1
    for ip in DisIP(group_name):
        try:
            id = id + 1
            row = row + 1
            subwin.addstr(row, 0, "| %s  " % id)
            subwin.addstr(row, 6, "| %s  " % ip)
            subwin.addstr(row, 30, "|")
            if len(DisIP(group_name)) == row:
                subwin.addstr(row + 2, 0, "+-----------------------------+")
            subwin.refresh()
        except :
            pass

    while 1:
        inch = subwin.getch()
        if inch != -1:
            try:
                instr = chr(inch)
            except:
                # just ignore non-character input
                pass
            else:
                if instr.upper() == 'Q':
                    break
        time.sleep(0.2)
    return subwin

def chooseUser(win, group_name='BJ'):
    pass

def mainloop(win):
    win.nodelay(1)  # disable getch() blocking
    # draw the main display template
    mainScreen(win)

    # run until the user wants to quit
    while 1:
        # check for keyboard input
        inch = win.getch()
        # getch() will return -1 if no character is available
        if inch != -1:
            # see if inch is really a character
            try:
                instr = str(chr(inch))
            except:
                # just ignore non-character input
                pass
            else:
                if instr.upper() == '1':
                    chooseIP(win, 'SH')
                    mainScreen(win)
                if instr.upper() == 'Q':
                    break
                if instr.upper() == 'W':
                    subwin = chooseIP(win)
                    # simple way to restore underlying main screan
                    mainScreen(win)
        WriteDateTime(win)
        getDataVals()
        writeDataVals(win)
        time.sleep(0.2)

def startup():
    # borrowed the idea of using a try-except wrapper around the
    # initialization from David Mertz.
    try:
        # Initialize curses
        stdscr = curses.initscr()

        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho()
        curses.cbreak()

        mainloop(stdscr)                # Enter the main loop

        # Set everything back to normal
        curses.echo()
        curses.nocbreak()

        curses.endwin()                 # Terminate curses
    except:
        # In event of error, restore terminal to sane state.
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception

if __name__=='__main__':
    startup()
