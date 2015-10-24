"""
Boo application
"""

import dev.motor
import random
import time


class boo(object):
    """
    Boo application module.
    """

    FORWARD = 0
    REVERSE = 1

    MINPOSITION = 1
    MAXPOSITION = 50

    def __init__(self, minm, maxm, minw, maxw, signal1, signal2):
        """
        Creates a boo application
        """
        self._ghost = dev.motor.motor(signal1, signal2)
        self._minmove = minm
        self._maxmove = maxm
        self._minwait = minw
        self._maxwait = maxw
        self._position = 0
        self._direction = boo.FORWARD


    def _getNewDirection(self):
        return random.randint(boo.FORWARD,boo.REVERSE)

    def loop(self):
        """
        Runs one application iteration.
        Returns whether application has finished or not.
        """
        wait =random.randint(self._minwait, self._maxwait)
        move =random.randint(self._minmove, self._maxmove)
        print 'position: ' + str(self._position)
	print 'waiting: ' + str(wait)
        time.sleep(wait)
        if self._direction == boo.FORWARD:
            self._position += move
            if self._position > boo.MAXPOSITION:
                self._position = boo.MAXPOSITION - 1

            print 'moving forward: ' + str(move)
            self._ghost.forward()
            time.sleep(move)
            self._ghost.stop()
        else:
            self._position -= move
            if self._position < boo.MINPOSITION:
                self._position = boo.MINPOSITION + 1

            print 'moving reverse: ' + str(move)
            self._ghost.reverse()
            time.sleep(move)
            self._ghost.stop()

        self._direction = self._getNewDirection()

        return False

