from gpiozero import DistanceSensor, LED
from time import sleep

def hello():
	print('Hello')
	led.on()


def bye():
	print('Bye')
	led.off()


ultrasonic = DistanceSensor(echo=15, trigger=14, threshold_distance=0.1)

ultrasonic.when_in_range = hello
ultrasonic.when_out_of_range = bye

led = LED(4)

while True:
	print(f'Distance: {ultrasonic.distance*100} cm')
	sleep(1)
