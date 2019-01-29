from urllib2 import urlopen
import time
from gpiozero import LightSensor, Buzzer

hostname="192.168.42.3:5000"
ldr = LightSensor(4)
led = Buzzer(17)

def httpconnect(action):
	url="http://{}/{}".format(hostname,action)
	try:
		print(urlopen(url).read().decode())
	except:
		print("Verbinding naar {} kon niet gemaakt worden".format(url))
		exit()
		
while True:
	time.sleep(0.9)
	print("LDR value: " + str(ldr.value))
	if o\0.5 > ldr.value:
		led.on()
		httpconnect("vol")
	else:
		led.off()
		httpconnect("nietvol")