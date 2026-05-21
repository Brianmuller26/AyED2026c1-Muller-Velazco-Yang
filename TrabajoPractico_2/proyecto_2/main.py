import time
import datetime
import random
from modules.temperatura import Temperaturas_DB 


muestras_temperatura = Temperaturas_DB()

if __name__ == "__main__":
    with open('data/muestras.txt', 'r') as archivo:
        for linea in archivo:
            # Ignora el prefijo si existe y limpia espacios
            linea = linea.replace('', '').strip()
            if linea:
                fecha, temp = linea.split(';')
                fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
                muestras_temperatura.guardar_temperatura(float(temp), fecha)
    fecha = "09/02/2025"
    fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    print(muestras_temperatura.devolver_temperatura(fecha))



    

