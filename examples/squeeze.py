"""
'squeeze.py'.

=================================================
<<<<<<< HEAD
using a force sensitive resistor (fsr) with CircuitPython
=======
force sensitive resistor (fsr) with circuitpython
>>>>>>> adafruit/master
"""

import analogio
import board
import pulseio

<<<<<<< HEAD
fsr = analogio.AnalogIn(board.A2)
led = pulseio.PWMOut(board.D10)

while True:
    led.duty_cycle = fsr.value
=======
FORCE_SENS_RESISTOR = analogio.AnalogIn(board.A2)
LED = pulseio.PWMOut(board.D10)

while True:
    LED.duty_cycle = FORCE_SENS_RESISTOR.value
>>>>>>> adafruit/master
