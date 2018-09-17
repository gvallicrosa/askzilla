import random
import time

class Chooser(object):
    def __init__(self, qlist):
        """Init with a question list."""
        self.qlist = qlist
        self.num = len(qlist) - 1
        self.reset()
    def reset(self):
        """Reset to initial state."""
        self.done = list()
        random.seed(time.time())
    def choose(self):
        while True:
            r = random.randint(0, self.num)
            if r not in self.done:
                self.done.append(r)
                return self.qlist[r]