import random

def ordenamiento_burbuja(lis):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.

    Args:
        lis (list): lista de números (int o float)

    Pre:
        - lis debe ser una lista
        - los elementos de la lista deben ser comparables entre sí

    Post:
        - la lista queda ordenada de menor a mayor
        - se conserva la misma cantidad de elementos
        - no se agregan ni eliminan elementos de la lista

    Returns:
        list: la misma lista ordenada de menor a mayor

    Raises:
        TypeError: si existen elementos en la lista que no pueden
        compararse entre sí
    """
     
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
    lis_sort = sorted(ejemplo_lis)
    lis_ordenada = ordenamiento_burbuja(ejemplo_lis)
    if lis_sort == lis_ordenada:
        print("La lista esta ordenanda correctamente ")