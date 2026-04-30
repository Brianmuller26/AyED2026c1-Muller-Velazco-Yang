import random

def ordenamiento_radix(lis):
    """
    Ordena una lista de números enteros positivos utilizando
    el algoritmo Radix Sort.

    Args:
        lis (list): lista de números enteros positivos.

    Pre:
        - lis debe ser una lista
        - todos los elementos deben ser números enteros positivos
        - los números deben tener como máximo 5 dígitos

    Post:
        - la lista queda ordenada de menor a mayor
        - se conservan todos los elementos originales
        - no se modifica la cantidad de elementos

    Returns:
        list: la misma lista ordenada de menor a mayor.

    Raises:
        TypeError: si existen elementos que no son enteros.
    """

    if len(lis) == 0:
        return lis
    
    max_num = max(lis)
    exp = 1
    
    for _ in range(5):
        lista_aux = [[] for _ in range(10)]
        pos = 0

        for num in lis:
            digit = (num // exp) % 10
            lista_aux[digit].append(num)
        
        pos_sgte = 0

        for sub_lis in lista_aux:
            for num in sub_lis:
                lis[pos_sgte]= num
                pos_sgte += 1
        exp*=10
    return lis

if __name__ == "__main__":
    # Prueba del algoritmo de ordenamiento radix
    ejemplo_lis = []
    for i in range(500):
        numero = random.randint(10000, 99999)
        ejemplo_lis.append(numero)
    lis_sort = sorted(ejemplo_lis)
    lis_ordenada = ordenamiento_radix(ejemplo_lis)
    if lis_sort == lis_ordenada:
        print("La lista esta ordenanda correctamente ")
     