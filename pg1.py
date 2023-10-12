from gpiozero import LED
from time import sleep

# Puerto de los LED
ledVerde = LED(17)
ledAzul = LED(27)
ledRojo = LED(22)

# Blucle para que parpade el led
while True:
    ledVerde.on()
    sleep(1)
    ledVerde.off()
    sleep(1)