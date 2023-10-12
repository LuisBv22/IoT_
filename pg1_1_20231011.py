# Actividad 2
# Ingresar desde la terminar que color se quiere prender utilizando biblioteca
import json
from gpiozero import LED
from time import sleep

colores = {"verde":True, "azul":True, "rojo":True}
accion = {"prendido":True, "apagado":True}


seleccion = "hola"
selec = "xd"

# Puerto de los LED
ledVerde = LED(17)
ledAzul = LED(27)
ledRojo = LED(22)

while True:
    print('Que color quieres utilziar: ')
    print('1. Rojo')
    print('2. Azul')
    print('3. Verde')
    
    input(seleccion)
    
    if True == colores[seleccion]:
        print('¿Que quieres hacer?')
        print('1. Prender')
        print('2. Apagar')
        input(selec)
    
        if seleccion == "verde":
            if True == accion[selec]:
                if selec == "Parpadear":
                    while True:
                        ledVerde.on()
                        sleep(1)
                        ledVerde.off()
                        sleep(1)
                else:
                    ledVerde.on()
        if seleccion == "azul":
            if True == accion[selec]:
                if selec == "Parpadear":
                    while True:
                        ledAzul.on()
                        sleep(1)
                        ledAzul.off()
                        sleep(1)
                else:
                    ledAzul.on()
        if seleccion == "rojo":
            if True == accion[selec]:
                if selec == "Parpadear":
                    while True:
                        ledRojo.on()
                        sleep(1)
                        ledRojo.off()
                        sleep(1)
                else:
                    ledRojo.on()
                            
                
                
            

        
        
