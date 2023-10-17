"""
1)Crear un programa que enciaenda LEDSs del RB en base a lo siguiente:
    Cuando el procesador se encuentre en menos del 10% de cpu (Verde estatico)
    Entre el 10% y el 20% (Amarillo estatico)
    Arriba del 20% (Rojo Parpadeante)

2)Crear otro programa que lea información de la nube constantemente (libreria request) y calcule el promedio de temperatura.
Esto a manera que simile el comportamiento de nuestro cpu 
"""

import psutil
from gpiozero import LED
from time import sleep
import requests

Porcentaje_cpu=0

ledverde = LED(17)
ledamarillo = LED(27)
ledrojo = LED(22)

while(True):
   
   #En caso de emular el CPU con una peticion recuerda de tener el archico Cpu.php en una pagina localhost o redireccionado en iun sistema que te regrese un valor 

   numero = requests.get('http://localhost:8888/Cpu.php')
   Porcentaje = int(numero.text)

   #en caso de que requiere el CPU que ejecuat el programa
   #Porcentaje = psutil.cpu_count()
   print(Porcentaje)

   #Condicionamos para encender el Led

   if Porcentaje <= 10:
  
      ledverde.on()
      #se apagaran los demas leds
      ledamarillo.off()
      ledrojo.off()
      sleep(5)
   
   if Porcentaje >10 and Porcentaje < 20:
   
      ledamarillo.on()
      #se apagarn los demas leds
      ledverde.off()
      ledrojo.off()
      sleep(5)
  
   if Porcentaje > 20:
      
      #se apagarn los demas leds
      ledverde.off()
      ledamarillo.off()

      while(True):

         ledrojo.on()
         sleep(1)
         ledrojo.off()
         sleep(1)
         
         if(psutil.cpu_count()<20):
            break
      
      
      
