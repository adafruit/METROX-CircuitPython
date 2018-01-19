"""
'char_LCD.py'
=================================================
hello world using 16x2 character LCD
requires:
- CircuitPython_CharLCD Module
"""

import time
import digitalio
import adafruit_character_lcd
from board import D7, D8, D9, D10, D11, D12, D13

#   Character LCD Config:
#   modify this if you have a different sized charLCD
LCD_COLUMNS = 16
LCD_ROWS = 2

#   Metro Express Pin Config:
LCD_RS = digitalio.DigitalInOut(D7)
LCD_EN = digitalio.DigitalInOut(D8)
LCD_D7 = digitalio.DigitalInOut(D12)
LCD_D6 = digitalio.DigitalInOut(D11)
LCD_D5 = digitalio.DigitalInOut(D10)
LCD_D4 = digitalio.DigitalInOut(D9)
LCD_BACKLIGHT = digitalio.DigitalInOut(D13)

#   Init the LCD class
LCD = adafruit_character_lcd.Character_LCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6,
                                           LCD_D7, LCD_COLUMNS, LCD_ROWS, LCD_BACKLIGHT)

#   Print a 2x line message
LCD.message('hello\ncircuitpython')
# Wait 5s
time.sleep(5)
#   Demo showing cursor
LCD.clear()
LCD.show_cursor(True)
LCD.message('showing cursor ')
#   Wait 5s
time.sleep(5)
#   Demo showing the blinking cursor
LCD.clear()
LCD.blink(True)
LCD.message('Blinky Cursor!')
#   Wait 5s
time.sleep(5)
LCD.blink(False)
#   Demo scrolling message LEFT
LCD.clear()
SCROLL_MSG = 'Scroll'
LCD.message(SCROLL_MSG)
#   Scroll to the left
for i in range(LCD_COLUMNS - len(SCROLL_MSG)):
    time.sleep(0.5)
    LCD.move_left()
#   Demo turning backlight off
LCD.clear()
LCD.message("going to sleep\ncya later!")
LCD.set_backlight(False)
time.sleep(2)
