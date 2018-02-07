"""
'mib_photo_sensor_night_light_sensor.py'.

=================================================
turns off and on a led using a photo sensor
"""

import analogio
import board
import digitalio

<<<<<<< HEAD
led = digitalio.DigitalInOut(board.D9)
light_sensor = analogio.AnalogIn(board.A0)
led.switch_to_output()

threshold_value = 60000
=======
threshold_value = 60000

led = digitalio.DigitalInOut(board.D9)
led.switch_to_output()
light_sensor = analogio.AnalogIn(board.A0)
>>>>>>> adafruit/master


while True:
    if light_sensor.value > threshold_value:
        led.value = True
    else:
        led.value = False
