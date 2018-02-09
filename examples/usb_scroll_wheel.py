"""
'usb_scroll_wheel.py'.

=================================================
usb-hid scroll-wheel with circuitpython

requires:
- simpleio library
- adafruit_character_lcd library
"""
import time
from board import D6, A0
from simpleio import map_range
import analogio
import adafruit_hid
import digitalio

m = adafruit_hid.Mouse()

button = digitalio.DigitalInOut(D6)
button.direction = digitalio.Direction.INPUT
pot = analogio.AnalogIn(A0)


while True:
    # move while button is pressed
    if not button.value:
        m.move(-1, 1, int(map_range(pot.value, 50, 65520, -5, 5)))
        time.sleep(.1)
