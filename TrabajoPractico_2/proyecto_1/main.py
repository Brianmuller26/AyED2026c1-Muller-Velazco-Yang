# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
from ayedfiuner.estructuras.monticulo import MonticuloBinario
import random

n = 5  # cantidad de ciclos de simulación

cola_de_espera = MonticuloBinario()
bucle = 0
i = 0
pacientes = 0
# Ciclo que gestiona la simulación
while bucle == 0:
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')  
    print('\n', fecha_y_hora, '\n')

    if i <= n:
        paciente = pac.Paciente()
        cola_de_espera.insertar(paciente)
        i += 1

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminarMin()
        print('Se atiende el paciente:', paciente_atendido)
        pacientes += 1

    else:
        pass # se continúa atendiendo paciente de ciclo anterior

    print('Pacientes que faltan atenderse:', len(cola_de_espera)) # Se muestran los pacientes restantes en la cola de espera
    for paciente in cola_de_espera:
        print('\t', paciente)

    time.sleep(1)

    if pacientes == n:
        bucle = 1
    

