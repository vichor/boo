Raspberry Boo application. 

This application will, at random intervals among given thresholds, move a ghost
from right to left or left to right while making a spooky booo sound through 
the speakers.

The ghost is pending from a elliptical thread having two poles, each one at one
of the edges of the long radius. One of the poles is attached to a motor which 
will be used to move the ghost

     +-------+                                              +-------+
      \     /                                                \     /
       |==================================+=======================|
      /     \                            /                   /     \
     +---+---+                          /                   +-------+
         |                          +--+--+
         |               --------  /     . \
       +---+           --------   /        /
       | M |         ---------   /        /
       +-+-+                    +        /
         |                       \/\/\/\+
         |
         |
       +---+
       | R |
       +---+

    M - motor
    R - Raspberry

HOWTO
=====

You will need an L9110 based H Bridge (see doc folder for datasheet).
Connect the forward h-brdige pin to Raspberry GPIO 20.
Connect the reverse h-brdige pin to Raspberry GPIO 21.
Connect the Vcc and GND h-bridge pins to Raspberry Vcc(5v) and Gnd respectively.
From the command line launch:
    $ sudo python boo
Enjoy!

DESIGN
======
This is a very simple application which actually can be created on a single file
with few lines. Design though, has been a bit more complicated to ilustrate the
usage of layers in software design. There are three layers:

app - implements what actually is required from a high level point of view. It
      does not care about how things are done, but about what needs to be done.
      For instance, it requests the motor to move forwards or backwards, without
      keeping in mind what needs to be done to achive this goal.
dev - Device abstraction layer. Any device used by the application will have
      a definition in this layer. There will be an hbridge which will drive
      the motor, thus, a class representing this hbridge will be found in this
      layer.
hal - Hardware abstraction layer. Access to very low level devices such as GPIOs
      pins.


Author: Victor Garcia
