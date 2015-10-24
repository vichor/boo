"""
gpio.py -   Access to GPIO pins through different interfaces.
"""

OUTPUT="out"
INPUT="in"

HIGH=1
LOW=0

class sysfsgpio(object):
    """
    Identifies a GPIO pin which can be accessed through sys fs interface.
    """

    # class attributes

    # list of all gpios being controlled
    _gpios = list()

    def __init__(self, gpio, direction, init=None):
        """
        Creates and enables access to a GPIO pin through sys fs interface.
            gpio - GPIO pin number
            direction - either gpio.OUTPUT or gpio.INPUT
            init - init value when defining an OUTPUT gpio. Mandatory when
                   creating an OUTPUT gpio.
        """
        assert(gpio not in sysfsgpio._gpios)
        assert(direction==OUTPUT or direction==INPUT)
        if direction == OUTPUT:
            assert(init!=None)

        # grab parameters to attributes
        self._gpio = gpio
        self._direction = direction

        # get access to pin
        fexport = open('/sys/class/gpio/export','w')
        fexport.write(str(self._gpio))
        fexport.close()

        # configure direction of pin
        fdirection = open('/sys/class/gpio/gpio'+str(self._gpio)+'/direction','w')
        fdirection.write(str(self._direction))
        fdirection.close()

        # initial access to pin, either read or write it
        if self._direction == OUTPUT: self.setgpio(init)
        else: self._value = self.getgpio()

        # add gpio to list of controlled ones
        sysfsgpio._gpios.append(self._gpio)

    def __del__(self):
        """
        Destroys the gpio
        """
        self.release()
        try: sysfsgpio._gpios.remove(self._gpio)
        except: pass

    def setgpio(self, value):
        """
        Sets the pin to a given value. The pin has to be created as OUTPUT.
        """
        assert(self._direction==OUTPUT)
        self._value = value
        fvalue = open('/sys/class/gpio/gpio'+str(self._gpio)+'/value','w')
        fvalue.write(str(self._value))
        fvalue.close()

    def getgpio(self):
        """
        Gets the pin value. The pin has to be created as INPUT, otherwise it
        will return last written value (won't be reading the pin actual value).
        """
        if self._direction == INPUT:
            fvalue = open('/sys/class/gpio/gpio'+str(self._gpio)+'/value','r')
            self._value = fvalue.read()
            fvalue.close()
        return self._value

    def release(self):
        """
        Releases access to gpio. It won't be able to be accessed anymore.
        """
        funexport = open('/sys/class/gpio/unexport','w')
        funexport.write(str(self._gpio))
        funexport.close()


class outpin(sysfsgpio):
    """
    Output GPIO access.
    """
    def __init__(self, gpio, init): super(outpin, self).__init__(gpio, OUTPUT, init)
    def write(self, value): super(outpin, self).setgpio(value)
    def read(self): return super(outpin, self).getgpio()


class inpin(sysfsgpio):
    """
    Input GPIO access.
    """
    def __init__(self, gpio): super(inpin, self).__init__(gpio, INPUT)
    def read(self): return super(inpin, self).getgpio()


