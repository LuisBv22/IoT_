
from gpiozero import LED, DistanceSensor
from time import sleep

trigPin = 9
echoPin = 11
pines = [17,27,22]
leds = [LED(x) for x in pines]
ultrasonico = DistanceSensor(echo=echoPin, trigger=trigPin)

while True:
    distancia = ultrasonico.distance*100
    print(distancia)
    if distancia < 5:
        leds[0].blink()
        leds[1].blink()
        leds[2].blink()
        sleep(0.3)
    if distancia < 10:
        leds[0].on()
        leds[1].on()
        leds[2].on()
    elif distancia < 50:
        leds[0].on()
        leds[1].on()
        leds[2].off()
    elif distancia < 100:
        leds[0].on()
        leds[1].off()
        leds[2].off()
    else:
        for l in leds:
            l.off()



