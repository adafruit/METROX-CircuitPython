"""
'photo_sensor.py'.

=================================================
<<<<<<< HEAD
uses a photo sensor to control a led
=======
uses LIGHT to control a LED
>>>>>>> adafruit/master
"""
import analogio
import board
import pulseio
from simpleio import map_range

<<<<<<< HEAD
led = pulseio.PWMOut(board.D9)
photo_sensor = analogio.AnalogIn(board.A0)


while True:
    photo_sensor_val = map_range(photo_sensor.value, 20000, 32766, 0, 32766)
    led.duty_cycle = int(photo_sensor_val)
=======
LED = pulseio.PWMOut(board.D9)
LIGHT = analogio.AnalogIn(board.A0)


while True:
    LIGHT_VAL = map_range(LIGHT.value, 20000, 32766, 0, 32766)
    LED.duty_cycle = int(LIGHT_VAL)
>>>>>>> adafruit/master
