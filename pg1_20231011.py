## Actividad 1
# Conecta LEd de 3 colores (RGB) diferentes en Raspberry (RB)
# Crear un programa que encienda el LED verde cuando corra y lo dej parpadeando
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