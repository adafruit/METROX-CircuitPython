"""
'mib_servo.py'.

=================================================
<<<<<<< HEAD
sweeping a servo with an analog potntiometer
=======
sweeping a servo with an analog potentiometer
>>>>>>> adafruit/master
requires:
- Adafruit_CircuitPython_Motor
"""
import time
import analogio
import board
import pulseio
from adafruit_motor import servo


<<<<<<< HEAD
servo = servo.servo(pulseio.PWMOut(board.D9))
pot = analogio.AnalogIn(board.A0)
=======
SERVO = servo.Servo(pulseio.PWMOut(board.D9))
POTE = analogio.AnalogIn(board.A0)
>>>>>>> adafruit/master


def servo_sweep():
    """sweeps the servo."""
    for angle_fwd in range(0, 180, 1):
<<<<<<< HEAD
        servo.angle = angle_fwd
        time.sleep(0.01)
    for angle_bkwd in range(180, 0, -1):
        servo.angle = angle_bkwd
        time.sleep(0.01)


def pot_sweep():
    """assigns servo value to an analog potntiometer value."""
    val = pot.value / 65536
    servo.angle = 180 * val
=======
        SERVO.angle = angle_fwd
        time.sleep(0.01)
    for angle_bkwd in range(180, 0, -1):
        SERVO.angle = angle_bkwd
        time.sleep(0.01)


def pote_sweep():
    """assigns servo value to an analog potentiometer value."""
    val = POTE.value / 65536
    SERVO.angle = 180 * val
>>>>>>> adafruit/master
    time.sleep(0.05)


while True:
    servo_sweep()
<<<<<<< HEAD
    # pot_sweep()
=======
    # pote_sweep()
>>>>>>> adafruit/master
