"""
<<<<<<< HEAD
'mib_potentiometer_light_thresh.py'.

=================================================
turns on a led when the potentiometer is above a half-turn
=======
'mib_potentiometer_THRESHOLD.py'.

=================================================
turns on a LED when the potentiometer is above a half-turn
>>>>>>> adafruit/master
"""
import analogio
import board
import digitalio

<<<<<<< HEAD
led = digitalio.DigitalInOut(board.D13)
pot = analogio.AnalogIn(board.A0)
led.switch_to_output()

light_thresh = 10000

while True:
    if pot.value > light_thresh:
        led.value = True
    else:
        led.value = False
=======
LED = digitalio.DigitalInOut(board.D13)
LED.switch_to_output()
POT = analogio.AnalogIn(board.A0)

THRESHOLD = 10000

while True:
    if POT.value > THRESHOLD:
        LED.value = True
    else:
        LED.value = False
>>>>>>> adafruit/master
