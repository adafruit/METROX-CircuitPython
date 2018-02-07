"""
'relay.py'.

=================================================
drives a small relay
"""

import time
import board
import digitalio

<<<<<<< HEAD
relay = digitalio.DigitalInOut(board.D2)
relay.switch_to_output()

while True:
    relay.value = not relay.value
=======
RELAY = digitalio.DigitalInOut(board.D2)
RELAY.switch_to_output()

while True:
    RELAY.value = not RELAY.value
>>>>>>> adafruit/master
    time.sleep(1)
