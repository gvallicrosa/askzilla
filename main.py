#!/usr/bin/env python

from __future__ import print_function
import curses
import time
from chooser import Chooser
from question import Question
from config import questions, WAIT_TIME, TOTAL_VALID

logo = (
"                       ^\   ^                 \n"
"                       / \\  / \                \n"
"                      /.  \\/   \      |\___/|  \n"
"   *----*           / / |  \\    \  __/  O  O\  \n"
"   |   /          /  /  |   \\    \_\/  \     \ \n"
"  / /\/         /   /   |    \\   _\/    '@___@ \n"
" /  /         /    /    |     \\ _\/       |U   \n"
" |  |       /     /     |      \\\/        |    \n"
" \  |     /_     /      |       \\  )   \ _|_   \n"
" \   \       ~-./_ _    |    .- ; (  \_ _ _,\'  \n"
" ~    ~.           .-~-.|.-*      _        {-,  \n"
"  \      ~-. _ .-~                 \      /\'   \n"
"   \                   }            {   .*      \n"
"    ~.                 '-/        /.-~----.     \n"
"      ~- _             /        >..----.\\\     \n"
"          ~ - - - - ^}_ _ _ _ _ _ _.-\\\        "
)

name = (
"      / _ \    | |  |___  (_) | |       \n"
"      / /_\ \___| | __  / / _| | | __ _  \n"
"      |  _  / __| |/ / / / | | | |/ _` | \n"
"      | | | \__ \   <./ /__| | | | (_| | \n"
"      \_| |_/___/_|\_\_____/_|_|_|\__,_| "
)

def main(stdscr):
    # Clear
    stdscr.clear()
    curses.echo()
    # Show name and logo
    stdscr.addstr(1, 1, name, curses.A_BLINK)
    stdscr.addstr(7, 1, logo)
    stdscr.refresh()
    # Question window
    win = curses.newwin(10, 70, 10, 50)
    # Show instructions
    win.clear()
    win.addstr(1, 1, (
        "Heu d'anar responent preguntes fins que n'encerteu {:d} seguides.\n"
        " Les preguntes es trien aleatoriament cada vegada que comenceu.\n"
        " Si falleu haureu d'esperar {:d} segons (aprofiteu aquest temps).\n"
        " Les respostes son una sola paraula o numero (sense espais)."
        "\n\n         Premeu [Enter] per iniciar..."
        ).format(TOTAL_VALID, WAIT_TIME))
    s = win.getstr(6, 1)

    # Start asking
    cho = Chooser(questions)
    valid = 0
    while valid < TOTAL_VALID:
        # Start fresh
        win.clear()
        # Header
        win.addstr(1, 1, "Encertat {:d}/{:d}".format(valid, TOTAL_VALID))
        # Ask
        q = Question(cho.choose(), win)
        ok = q.ask()
        if ok:
            valid += 1
            # Show success
            win.clear()
            win.addstr(1, 1, "Correcte")
            win.refresh()
            time.sleep(2)
        else:
            cho.reset()
            valid = 0
            # Sound
            print('\a')  # bell alarm
            # Show fail and wait
            for i in range(WAIT_TIME):
                win.clear()
                win.addstr(1, 1, "Incorrecte. Espera {:d} segons...".format(WAIT_TIME - i))
                win.refresh()
                time.sleep(1)
    # Winner
    win.clear()
    win.addstr(5, 1, "Heu superat el repte !!", curses.A_BLINK)
    win.refresh()
    time.sleep(10)
        
# correct terminal reset
curses.wrapper(main)