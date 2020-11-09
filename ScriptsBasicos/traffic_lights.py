from gpiozero import Button, TrafficLights
from time import sleep

button = Button(17)
lights = TrafficLights(2, 3, 4)

while True:
	button.wait_for_press()
	lights.green.on()
	sleep(1)
	lights.amber.on()
	sleep(1)
	lights.red.on()
	sleep(1)
	lights.off()

