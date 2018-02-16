"""
'thermometer.py'.

=================================================
digital thermometer project using a tmp36 and a character lcd!

requires:
- simpleio library
- adafruit_character_lcd library
"""

import time
import digitalio
import analogio
import adafruit_character_lcd
from simpleio import map_range
from board import A0, D7, D8, D9, D10, D11, D12, D13

#   Character LCD Config:
#   modify this if you have a different sized charlcd
lcd_columns = 16
lcd_rows = 2

#   Metro Express Pin Config:
lcd_rs = digitalio.DigitalInOut(D7)
lcd_en = digitalio.DigitalInOut(D8)
lcd_d7 = digitalio.DigitalInOut(D12)
lcd_d6 = digitalio.DigitalInOut(D11)
lcd_d5 = digitalio.DigitalInOut(D10)
lcd_d4 = digitalio.DigitalInOut(D9)
lcd_backlight = digitalio.DigitalInOut(D13)

#   Init the lcd class
lcd = adafruit_character_lcd.Character_LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                           lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

therm = analogio.AnalogIn(A0)

while True:
    tmp = (((map_range(therm.value, 0, 65535, 0, 3.3))-.5)*100)
    lcd.clear()
    lcd.message('temp: ' + str(tmp)[:5] + ' * C')
    time.sleep(.6)
