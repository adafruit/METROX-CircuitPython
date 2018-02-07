"""
'potentiometer.py'.

=================================================
<<<<<<< HEAD
control a led's brightness using a potentiometer
=======
control a LED's brightness using a potentiometer
>>>>>>> adafruit/master
"""
import time
import digitalio
import analogio
import board

<<<<<<< HEAD
led = digitalio.DigitalInOut(board.D13)
pot = analogio.AnalogIn(board.A0)
led.switch_to_output()

sensor_val = 0

while True:
    # potentiometer value/max potentiometer value
    sensor_val = pot.value / 65536
    print(sensor_val)
    led.value = True
    time.sleep(sensor_val)
    led.value = False
    time.sleep(sensor_val)
=======
LED = digitalio.DigitalInOut(board.D13)
LED.switch_to_output()
POT = analogio.AnalogIn(board.A0)

SENSOR_VAL = 0

while True:
    # potentiometer value/max potentiometer value
    SENSOR_VAL = POT.value / 65536
    print(SENSOR_VAL)
    LED.value = True
    time.sleep(SENSOR_VAL)
    LED.value = False
    time.sleep(SENSOR_VAL)
>>>>>>> adafruit/master
