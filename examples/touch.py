"""
'touch.py'
=================================================
capactive touch with the Adafruit Metro
requires:
- touchio
"""

import time
from board import D13, A1
import digitalio
import touchio

led = digitalio.DigitalInOut(D13)
led.switch_to_output()
touch = touchio.TouchIn(A1)

while True:
    # if the capacitive pin is touched
    if touch.value:
        led.value = True
    else:
        led.value = False
    time.sleep(1)
