"""
'mib_char_LCD_light.py'
=================================================
light sensor circuit. displays output on charLCD
requires:
- CircuitPython_CharLCD Module
"""

import time
import analogio
import digitalio
import adafruit_character_lcd
from board import D7, D8, D9, D10, D11, D12, D13, A0

#   Character LCD Config:
#   modify this if you have a different sized charLCD
LCD_COLS = 16
LCD_ROWS = 2

#   Metro Express Pin Config:
LCD_RS = digitalio.DigitalInOut(D7)
LCD_EN = digitalio.DigitalInOut(D8)
LCD_D7 = digitalio.DigitalInOut(D12)
LCD_D6 = digitalio.DigitalInOut(D11)
LCD_D5 = digitalio.DigitalInOut(D10)
LCD_D4 = digitalio.DigitalInOut(D9)
LCD_BACKLIGHT = digitalio.DigitalInOut(D13)

LIGHT_SENSOR = analogio.AnalogIn(A0)

#   Init the LCD class
LCD = adafruit_character_lcd.Character_LCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6,
                                           LCD_D7, LCD_COLS, LCD_ROWS, LCD_BACKLIGHT)

while True:
    LCD.clear()
    LIGHT_VAL = str(100-((LIGHT_SENSOR.value/65535)*100))
    LIGHT_VAL_NICE = LIGHT_VAL[:LIGHT_VAL.find('.')]
    LCD.message(LIGHT_VAL_NICE + "% bright")
    LCD.message(str(LIGHT_SENSOR.value))
    time.sleep(1)
