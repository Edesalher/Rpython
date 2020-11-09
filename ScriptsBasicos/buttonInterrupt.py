from gpiozero import LED, Button

led1 = LED(2)
led2 = LED(3)
button = Button(4, True)

button.when_pressed = led2.on
button.when_released = led2.off

while True:
	led1.blink(1, 1, background=False)
