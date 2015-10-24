"""
hbridge.py - H bridge control.
"""

import hal.gpio as io

class hbridge(object):
    """
    Control for H-bridge drivers.
    """

    def __init__(self, pin1, pin2):
        """
        Creates a pololu motor control. Stops the motor.
            pin1 - pin control high. When set, motor moves forward.
            pin2 - pin control low. When set, motor moves reverse.
        """
        self._pinh = io.outpin(pin1,io.LOW)
        self._pinl = io.outpin(pin2,io.LOW)
        self.breakgnd()

    def forward(self):
        """
        Sets H Bridge to forward position
        """
        self._pinh.write(io.HIGH)
        self._pinl.write(io.LOW)

    def reverse(self, rpm=None):
        """
        Sets H Bridge to reverse position
        """
        self._pinh.write(io.LOW)
        self._pinl.write(io.HIGH)

    def breakgnd(self):
        """
        Breaks H bridge to ground.
        """
        self._pinh.write(io.LOW)
        self._pinl.write(io.LOW)

    def breakvcc(self):
        """
        Breaks H bridge to battery/Vcc.
        """
        self._pinh.write(io.HI)
        self._pinl.write(io.HI)

