from gpiozero import LightSensor, Buzzer
from time import sleep

ldr = LightSensor(4)

led = Buzzer(17)

while True:
	sleep(0.9)
	if ldr.value < 0.5:
		led.on()
	else:
		led.off()