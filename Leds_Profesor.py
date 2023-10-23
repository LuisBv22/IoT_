
from gpiozero import LED, Button
from time import sleep

pinBot = 10
pines = [17,27,22]
Boton = Button(pinBot)
leds = [LED(x) for x in pines]
cont = 0

while True:
    leds[cont].on()
    leds[cont-1].off()
    leds[cont-2].off()
    
    if Boton.is_pressed:    
        cont += 1
        cont %= 3
        sleep(0.3)
