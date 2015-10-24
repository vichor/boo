"""
Boo application
"""

import dev
import random
import time


class boo(object):
    """
    Boo application module.
    """

    FORWARD = 0
    REVERSE = 1

    MINPOSITION = 0.5
    MAXPOSITION = 5

    def __init__(self, minm, maxm, minw, maxw, signal1, signal2):
        """
        Creates a boo application
        """
        self._ghost = dev.motor(signal1, signal2)
        self._minmove = minm
        self._maxmove = maxm
        self._minwait = minw
        self._maxwait = maxw
        self._position = 0
        self._direction = FORWARD


    def _getNewDirection(self):
        return random.randint(FORWARD,REVERSE)

    def loop(self):
        """
        Runs one application iteration.
        Returns whether application has finished or not.
        """
        wait =random.randint(self._minwait, self._maxwait)
        move =random.randint(self._minmove, self._maxmove)
        time.sleep(wait)
        if self._direction == FORWARD:
            self._position += move
            if self._position > MAXPOSITION:
                self._position = MAXPOSITION - 1

            self._ghost.forward()
            time.sleep(move)
            self._ghost.stop()
        else:
            self._position -= move
            if self._position < MINPOSITION:
                self._position = MINPOSITION + 1

            self._ghost.reverse()
            time.sleep(move)
            self._ghost.stop()

        self._direction = self._getNewDirection()

        return False








