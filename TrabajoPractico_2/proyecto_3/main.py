# import sys
# print(sys.executable)

import random
import time
import matplotlib.pyplot as plt

from ayedfiuner.algoritmos.burbuja import ordenamiento_burbuja
from ayedfiuner.algoritmos.quicksort import ordenamiento_quicksort
from ayedfiuner.algoritmos.radixsort import ordenamiento_radix

tamanios = [1, 100, 200, 300, 400, 500, 700, 900, 1000]

tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []
tiempos_sorted = []

for n in tamanios:
    
    for _ in range (n):
        lista = [random.randint(10000, 99999) for _ in range(n)]

#    Burbuja
    copia = lista.copy()
    inicio = time.perf_counter()
    ordenamiento_burbuja(copia)
    fin = time.perf_counter()
    tiempos_burbuja.append(fin - inicio)

#     Quicksort
    copia = lista.copy()
    inicio = time.perf_counter()
    ordenamiento_quicksort(copia)
    fin = time.perf_counter()
    tiempos_quick.append(fin - inicio)

#     Radix
    copia = lista.copy()
    inicio = time.perf_counter()
    ordenamiento_radix(copia)
    fin = time.perf_counter()
    tiempos_radix.append(fin - inicio)

# Comparamos con la función built-in sorted
    copia = lista.copy()
    inicio = time.perf_counter()
    sorted(copia)
    fin = time.perf_counter()
    tiempos_sorted.append(fin - inicio)

# Graficar
plt.plot(tamanios, tiempos_burbuja, label="Burbuja")
plt.plot(tamanios, tiempos_quick, label="Quicksort")
plt.plot(tamanios, tiempos_radix, label="Radix")
plt.plot(tamanios, tiempos_sorted, label="sorted()")

plt.xlabel("Cantidad de elementos (N)")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid()

plt.savefig("data/grafico_ordenamientos.png")
plt.show()