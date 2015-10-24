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

Author: Victor Garcia
