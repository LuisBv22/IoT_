from gpiozero import LED,Button
from time import sleep

# Puerto de los LED
ledVerde = LED(17)
ledAmarillo = LED(27)
ledRojo = LED(22)
boton = Button(10)

while True:

    if boton.is_pressed:
        if ledRojo.is_lit == False  and  ledAmarillo.is_lit == False and ledVerde.is_lit == False:
             ledVerde.on()
        
        if ledVerde.is_lit == True:
             ledVerde.off()
             ledAmarillo.on()
    
        if ledAmarillo.is_lit == True:
             ledAmarillo.off()
             ledRojo.on()

        if ledRojo.is_lit == True:
             ledRojo.off()
             ledVerde.on()
        