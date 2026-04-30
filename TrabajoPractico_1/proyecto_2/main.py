import time
import matplotlib.pyplot as plt
import random
from ayedfiuner.estructuras.LDE import ListaDobleEnlazada


N_lista = [100, 500, 1000, 5000, 10000]

tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in N_lista:
    lista = ListaDobleEnlazada()

    for _ in range(n):
        lista.agregar_al_final(random.randint(-100, 100))

    tic = time.perf_counter()
    len(lista)
    toc = time.perf_counter()
    tiempos_len.append(toc - tic)

    tic = time.perf_counter()
    lista.copiar()
    toc = time.perf_counter()
    tiempos_copiar.append(toc - tic)

    lista_aux = lista.copiar()
    tic = time.perf_counter()
    lista_aux.invertir()
    toc = time.perf_counter()
    tiempos_invertir.append(toc - tic)

plt.plot(N_lista, tiempos_len, label="len()")
plt.plot(N_lista, tiempos_copiar, label="copiar()")
plt.plot(N_lista, tiempos_invertir, label="invertir()")

plt.title("Tiempo de ejecución vs cantidad de elementos (N)")
plt.xlabel("Cantidad de elementos (N)")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid()

max_len = max(tiempos_len)
max_copiar = max(tiempos_copiar)
max_invertir = max(tiempos_invertir)

plt.scatter(N_lista[tiempos_len.index(max_len)], max_len)
plt.scatter(N_lista[tiempos_copiar.index(max_copiar)], max_copiar)
plt.scatter(N_lista[tiempos_invertir.index(max_invertir)], max_invertir)

plt.savefig("data/grafico_tiempos.png")
plt.show()