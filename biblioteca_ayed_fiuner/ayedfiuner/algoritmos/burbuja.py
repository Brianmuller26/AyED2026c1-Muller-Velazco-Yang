import random

def ordenamiento_burbuja(lis):
    for extremo in range(len(lis)-1, 0, -1):
        hubo_intercambio = False

        for i in range(extremo):
            if lis[i] > lis[i+1]:

                auxiliar = lis[i]
                lis[i] = lis[i+1]
                lis[i+1] = auxiliar

                hubo_intercambio = True
            
        #si no hay intercambio
        if not hubo_intercambio:
            break

    return lis   
    

if __name__ == "__main__":
    # Prueba del algoritmo de ordenamiento burbuja
    ejemplo_lis = []
    for i in range(500):
        numero = random.randint(10000, 99999)
        ejemplo_lis.append(numero)

    lis_ordenada = ordenamiento_burbuja(ejemplo_lis)
    print("Lista ordenada:", lis_ordenada)