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
                muestras_temperatura.guardar_temperatura(float(temp), fecha)
    # fecha = "17/02/2025"
    print("Devolver temperatura: ", muestras_temperatura.devolver_temperatura(fecha))

    """Ingrese el rango de fecha para devolver la temp máxima entre esas fechas"""
    fecha1 = "01/02/2025"  
    fecha2 = "07/04/2025"
    print("La temperatura maxima es de:", muestras_temperatura.max_temp_rango(fecha1,fecha2))

    fecha1 = "07/02/2025"  
    fecha2 = "01/03/2025"
    print("La temperatura minima es de:", muestras_temperatura.min_temp_rango(fecha1,fecha2))

    fecha1 = "07/01/2024"
    fecha2 = "01/04/2024"
    print("La temperatura minima y maxima es:", muestras_temperatura.temp_extremos_rango(fecha1,fecha2))

    fecha = "07/01/2025"
    print("La fecha de la cual se elimina la temperatura medida es: ", fecha)
    muestras_temperatura.borrar_temperatura(fecha)
    
    fecha1 = "02/01/2025"  
    fecha2 = "05/01/2025"
    print("Las temperaturas medidas en las fechas es:")
    for m in muestras_temperatura.devolver_temperaturas(fecha1,fecha2):
        print(m)
    
    print("La cantidad de muestras de la DB es: ", muestras_temperatura.cantidad_muestras())
