"""
Wiring:
RS --> Pin 15
RW --> Pin 18
E  --> Pin 16
DATA 4-7 --> Pin 21, 22, 23, 24
"""

from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

# Initializing the LCD.
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24], numbering_mode=GPIO.BOARD)
# Writing data
lcd.write_string('Test LCD 2x16')
lcd.cursor_pos = (1, 2)
lcd.write_string('Raspberry Pi 4')

# Closing the connection
lcd.close()
# lcd.close(clear=True)
