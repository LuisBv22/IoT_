"""
1)Crear un programa que enciaenda LEDSs del RB en base a lo siguiente:
    Cuando el procesador se encuentre en menos del 10% de cpu (Verde estatico)
    Entre el 10% y el 20% (Amarillo estatico)
    Arriba del 20% (Rojo Parpadeante)

2)Crear otro programa que lea información de la nube constantemente (libreria request) y calcule el promedio de temperatura.
Esto a manera que simile el comportamiento de nuestro cpu 
"""

import psutil
import gpiozero
import time
import requests

Porcentaje_cpu=0

ledverde=LED(17)
ledamarillo=LED(27)
ledrojo=LED(22)

while(True):
   
   #En caso de emular el CPU con una peticion recuerda de tener el archico Cpu.php en una pagina localhost o redireccionado en iun sistema que te regrese un valor 

   #Porcentaje = requests.get('http://10.87.29.33/Cpu.php')

   #en caso de que requiere el CPU que ejecuat el programa
   Porcentaje = psutil.cpu_count()

   #Condicionamos para encender el Led

   if Porcentaje <= 10:
  
      ledverde.on()
      #se apagaran los demas leds
      ledamarillo.off()
      ledrojo.off()
   
   if Porcentaje >10 and Porcentaje < 20:
   
      ledamarillo.on()
      #se apagarn los demas leds
      ledverde.off()
      ledrojo.off()
  
   if Porcentaje > 20:
      
      #se apagarn los demas leds
      ledverde.off()
      ledamarillo.off()

      while(True):
         ledrojo.on()
         ledrojo.off()
         if(psutil.cpu_count()<20):
            break
      
      
      
