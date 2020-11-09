from gpiozero import LED, Button
# from time import sleep
from signal import pause
import sys

led = LED(2)
button = Button(3)

try:
#	while True:
#		button.wait_for_press()
#		print('Pressed')
#		led.on()
#		button.wait_for_release()
#		print('Released')
#		led.off()
	button.when_pressed = led.on
	button.when_released = led.off
	pause()
except KeyboardInterrupt:
	sys.exit()
