from RPLCD.i2c import CharLCD
# import time

# Initializing the LCD.
lcd = CharLCD('PCF8574', 0x27)

# Writing data
lcd.write_string('Test LCD 2x16')
lcd.cursor_pos = (1, 2)
lcd.write_string('RPi 4 with I2C')
# time.sleep(3)

# Closing the connection
lcd.close()
# lcd.close(clear=True)

