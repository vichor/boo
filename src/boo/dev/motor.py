"""
motor.py - Motor control.
"""

import hbridge

class motor(object):
    """
    10:1 micro metal medium power gearmotor
    """

    def __init__(self, pin1, pin2):
        """
        Creates a pololu motor control. Stops the motor.
            pin1 - pin control forward.
            pin2 - pin control reverse.
        """
        self._bridge=hbridge.hbridge(pin1, pin2)
        self.stop()

    def forward(self, rpm=None):
        """
        Moves the motor forward.
        """
        if rpm==None:
            # full speed
            self._bridge.forward()

    def reverse(self, rpm=None):
        """
        Moves the motor reverse.
        """
        if rpm==None:
            # full speed
            self._bridge.reverse()

    def stop(self):
        """
        Stops the motor.
        """
        self._bridge.breakgnd()

