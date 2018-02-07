"""
'neopixel_builtin.py'.

=================================================
playing with the metro express builtin NeoPixel
"""

import time
import board
import neopixel

# we only have one neopixel on our metro express
<<<<<<< HEAD
metro_neopixel = neopixel.NeoPixel(board.metro_neopixelPIXEL, 1)
metro_neopixel.brightness = 0.5
=======
NEO = neopixel.NeoPixel(board.NEOPIXEL, 1)
NEO.brightness = 0.5
>>>>>>> adafruit/master

# primary colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

<<<<<<< HEAD
color_array = [RED, GREEN, BLUE]

for i in color_array:
    metro_neopixel[0] = i
    metro_neopixel.show()
=======
COLORS = [RED, GREEN, BLUE]

for i in COLORS:
    NEO[0] = i
    NEO.show()
>>>>>>> adafruit/master
    time.sleep(.3)

# shows all colors by trying all combinations of RGB levels
for red_level in range(0, 256, 100):
    for green_level in range(0, 256, 100):
        for blue_level in range(0, 256, 100):
            print("red: ", red_level, "green: ",
                  green_level, "blue: ", blue_level)
<<<<<<< HEAD
            metro_neopixel[0] = (red_level, green_level, blue_level)
            metro_neopixel.show()
            # wait 0.2 seconds to give us time to see the colors
            time.sleep(1)
metro_neopixel[0] = (0, 0, 0)
metro_neopixel.show()
=======
            NEO[0] = (red_level, green_level, blue_level)
            NEO.show()
            # wait 0.2 seconds to give us time to see the colors
            time.sleep(1)
NEO[0] = (0, 0, 0)
NEO.show()
>>>>>>> adafruit/master
