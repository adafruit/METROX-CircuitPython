"""
<<<<<<< HEAD
'motor.py'.

=================================================
spin a DC motor using digitalio
=======
'MOTOR.py'.

=================================================
spin a DC MOTOR using digitalio
>>>>>>> adafruit/master
"""

import time
import board
import digitalio

<<<<<<< HEAD
motor = digitalio.DigitalInOut(board.D9)
motor.switch_to_output()
=======
MOTOR_PIN = board.D9
MOTOR = digitalio.DigitalInOut(MOTOR_PIN)
MOTOR.switch_to_output()
>>>>>>> adafruit/master


def motor_on_then_off():
    """toggles the motor."""
    on_time = 2.5
    off_time = 1.0
<<<<<<< HEAD
    motor.value = True
    time.sleep(on_time)
    motor.value = False
=======
    MOTOR.value = True
    time.sleep(on_time)
    MOTOR.value = False
>>>>>>> adafruit/master
    time.sleep(off_time)


while True:
    motor_on_then_off()
