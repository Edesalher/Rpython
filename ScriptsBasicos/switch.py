from gpiozero import LED, Button
from time import sleep

led = LED(2)
button = Button(3)

while True:
	button.wait_for_press()
	led.toggle()
	sleep(0.5)

