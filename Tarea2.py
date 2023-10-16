import requests
from time import sleep

while(True):
    #Se hace una peticion a una Url para esperar su respuesta 
    respuesta = requests.get('http://localhost:8888/Cpu.php')

    print("Los grados de cpu son :" + respuesta.text)
    sleep(3)
