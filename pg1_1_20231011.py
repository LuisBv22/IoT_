# Actividad 2
# Ingresar desde la terminar que color se quiere prender utilizando biblioteca
import json
from gpiozero import LED
from time import sleep

colores = {"Verde":True, "Azul":True, "Rojo":True}
accion = {"Parpadear":True, "Prendido":True}


seleccion = "hola"
selec = "xd"
cantidad = 1

# Puerto de los LED
ledVerde = LED(17)
ledAzul = LED(27)
ledRojo = LED(22)

while True:
    print('Que color quieres utilziar: ')
    print('1. Rojo')
    print('2. Azul')
    print('3. Verde')
    
    seleccion = input()
    
    if True == colores[seleccion]:
        cantidad=0
        
        print('¿Que quieres hacer?')
        print('1. Parpadear')
        print('2. Prendido')
        selec = input()
    
        if seleccion == "Verde":
            if True == accion[selec]:
                if selec == "Parpadear":
                    
                    while cantidad != 5:
                        ledVerde.on()
                        sleep(1)
                        ledVerde.off()
                        sleep(1)
                        cantidad=cantidad+1
                else:
                    ledVerde.on()
        if seleccion == "Azul":
            if True == accion[selec]:
                if selec == "Parpadear":
                    while cantidad != 5:
                        ledAzul.on()
                        sleep(1)
                        ledAzul.off()
                        sleep(1)
                        cantidad=cantidad+1
                else:
                    ledAzul.on()
        if seleccion == "Rojo":
            if True == accion[selec]:
                if selec == "Parpadear":
                    while cantidad != 5:
                        ledRojo.on()
                        sleep(1)
                        ledRojo.off()
                        sleep(1)
                        cantidad=cantidad+1
                else:
                    ledRojo.on()
                            
                
                
            

        
        
