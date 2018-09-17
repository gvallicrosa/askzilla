import curses
import signal
import time

def timeout_handler(signal, frame):
    raise Exception('Time is up!')
def signal_handler(signal, frame):
    pass
signal.signal(signal.SIGALRM, timeout_handler)
signal.signal(signal.SIGINT, signal_handler)

class Question(object):
    def __init__(self, qlist, win):
        """Construct from [question, answer, timer], window"""
        self.question = qlist[0]
        self.answer = qlist[1].lower()
        self.time = qlist[2]
        self.win = win
    def check(self, answer):
        """Check answer."""
        answer = answer.lower()
        if answer == self.answer:
            return True
        return False
    def ask(self):
        """Ask with a timer."""
        signal.alarm(self.time)
        try:
            self.win.addstr(3, 1, "Temps: {:d}s".format(self.time), curses.A_BLINK)
            self.win.addstr(4, 1, self.question, curses.A_BOLD)
            s = ""
            while not s:
                s = self.win.getstr(6, 1)
            signal.alarm(0)  # disable
            return self.check(s)
        except:
            self.win.clear()
            self.win.addstr(1, 1, "Timeout")
            self.win.refresh()
            time.sleep(1)
            return False

        

