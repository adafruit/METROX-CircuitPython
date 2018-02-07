"""
'temperature.py'.

=================================================
<<<<<<< HEAD
Writes tmp_value36 data to the REPL
=======
Writes TMP36 data to the REPL
>>>>>>> adafruit/master
"""

import time
import analogio
import board
from simpleio import map_range

<<<<<<< HEAD
tmp36 = analogio.AnalogIn(board.A0)


def get_voltage(_temp_sensor):
    """gets the tmp_value36's voltage."""
=======
TEMP_SENSOR = analogio.AnalogIn(board.A0)


def get_voltage(_temp_sensor):
    """gets the TMP36's voltage."""
>>>>>>> adafruit/master
    voltage_val = map_range(_temp_sensor.value, 0, 65535, 0, 3.3)
    return voltage_val


while True:
<<<<<<< HEAD
    tmp_value = get_voltage(tmp36)
    print("Voltage =", tmp_value, end="")
    # convert to celsius
    tmp_value = (tmp_value - 0.5) * 100
    print("   Temperature =", tmp_value)
=======
    TMP = get_voltage(TEMP_SENSOR)
    print("Voltage =", TMP, end="")
    # convert to celsius
    TMP = (TMP - 0.5) * 100
    print("   Temperature =", TMP)
>>>>>>> adafruit/master
    time.sleep(1)
