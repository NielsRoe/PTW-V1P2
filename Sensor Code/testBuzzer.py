from gpiozero import Buzzer

led = Buzzer(17)
led.beep()