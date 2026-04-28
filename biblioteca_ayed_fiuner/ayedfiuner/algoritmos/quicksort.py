def ordenamiento_quicksort(lis):
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
    ejemplo_lis = [64, 34, 25, 12, 22, 11, 90]
    lis_ordenada = ordenamiento_quicksort(ejemplo_lis)
    print("Lista ordenada:", lis_ordenada)

