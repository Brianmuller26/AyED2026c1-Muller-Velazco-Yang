import random
def ordenamiento_quicksort(lis):
    """
    Ordena una lista de menor a mayor utilizando el algoritmo Quicksort.

    Args:
        lis (list): lista con elementos comparables entre sí.

    Pre:
        - lis debe ser una lista
        - los elementos deben poder compararse usando >, < y ==

    Post:
        - se devuelve una nueva lista ordenada de menor a mayor
        - la lista original no se modifica
        - se conservan todos los elementos originales

    Returns:
        list: una nueva lista ordenada de menor a mayor.

    Raises:
        TypeError: si existen elementos en la lista que no pueden
        compararse entre sí.
    """
    #Si la lista es 1 o menor, ya estaria ordenado, por lo tanto lo devolveria
    if len(lis) <= 1:
        return lis
    else:
        pivot = lis[len(lis) // 2]
        #Una lista para guardar provisoriamente los valores menores al pivot
        izquierda = [x for x in lis if x < pivot] 
        #Una lista que guarda los valores iguales al pivot, que es el medio
        medio = [x for x in lis if x == pivot] 
        #Una lista para guardar provisoriamente los valores mayores al pivot
        derecha = [x for x in lis if x > pivot]
        return ordenamiento_quicksort(izquierda) + medio + ordenamiento_quicksort(derecha)

if __name__ == "__main__":
    # Prueba local del algoritmo de ordenamiento quicksort
    ejemplo_lis = []
    for i in range(500):
        numero = random.randint(10000, 99999)
        ejemplo_lis.append(numero)
    lis_sort = sorted(ejemplo_lis)
    lis_ordenada = ordenamiento_quicksort(ejemplo_lis)
    
    if lis_sort == lis_ordenada:
        print("La lista esta ordenanda correctamente ")
