"""
'temp_value_alarm.py'.

=================================================
sounds an alarm when the temp_value crosses a threshold
requires:
- simpleio
"""

import time
import analogio
import board
import simpleio

tmp36 = analogio.AnalogIn(board.A0)

freeze_temp = 0
boiling_temp = 100


while True:
    temp_value = simpleio.map_range(tmp36.value, 0, 65535, 0, 5)
    # temp to degrees C
    temp_value = (temp_value - .5) * 100
    print(temp_value)

    if temp_value < freeze_temp:
        simpleio.tone(board.D8, 263, 2)
    if temp_value > boiling_temp:
        simpleio.tone(board.D8, 523, 2)
    time.sleep(.5)
