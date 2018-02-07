"""
<<<<<<< HEAD
'temp_value_alarm.py'.

=================================================
sounds an alarm when the temp_value crosses a threshold
=======
'TEMP_alarm.py'.

=================================================
sounds an alarm when the TEMP crosses a threshold
>>>>>>> adafruit/master
requires:
- simpleio
"""

import time
import analogio
import pulseio
import board
from simpleio import map_range

<<<<<<< HEAD
piezo = pulseio.PWMOut(board.D8, frequency=440, duty_cycle=0, variable_frequency=True)
tmp36 = analogio.AnalogIn(board.A0)

freeze_temp = 0
boiling_temp = 100

while True:
    temp_value = map_range(tmp36.value, 0, 65535, 0, 5)
    # temp to degrees C
    temp_value = (temp_value - .5) * 100
    print(temp_value)

    if temp_value < freeze_temp:
        piezo.duty_cycle = 30000
    if temp_value > boiling_temp:
        piezo.duty_cycle = 10000
=======
PIEZO = pulseio.PWMOut(board.D8, frequency=440, duty_cycle=0, variable_frequency=True)
TMP_36 = analogio.AnalogIn(board.A0)

FREEZING_TEMP = 0
BOIL_TEMP = 100

while True:
    TEMP = map_range(TMP_36.value, 0, 65535, 0, 5)
    # temp to degrees C
    TEMP = (TEMP - .5) * 100
    print(TEMP)

    if TEMP < FREEZING_TEMP:
        PIEZO.duty_cycle = 30000
    if TEMP > BOIL_TEMP:
        PIEZO.duty_cycle = 10000
>>>>>>> adafruit/master
    time.sleep(.5)
