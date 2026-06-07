class MonticuloBinario:
    
    def __init__(self):
        """
        Precondición:
        Ninguna.

        Postcondición:
        Se crea un montículo binario vacío.
        listaMonticulo contiene únicamente el elemento centinela 0.
        tamanoActual se inicializa en 0.
        """
        self.listaMonticulo = [0]
        self.tamanoActual = 0   

    def hijoMin(self, i):
        """
        Precondición:
        i debe ser un entero positivo.
        i debe corresponder a una posición válida dentro del montículo.

        Postcondición:
        Devuelve el índice del hijo con menor prioridad.
        No modifica la estructura del montículo.

        Excepciones:
        IndexError si i no corresponde a una posición válida.
        """
        #El i * 2 se refiere al hijo izquierdo y el i * 2+1 es el hijo izquierdo
        if i * 2 + 1 > self.tamanoActual:
            return i * 2 
        else:
            # Comparamos riesgos de los dos hijos
            if self.listaMonticulo[i*2].get_riesgo() < self.listaMonticulo[i*2+1].get_riesgo():
                return i * 2
            else:
                return i * 2 + 1
    
    def infiltArriba(self, i):
        """
        Precondición:
        i debe ser un entero positivo.
        i debe corresponder a una posición válida del montículo.

        Postcondición:
        El elemento ubicado en la posición i queda correctamente ubicado
        respetando la propiedad de montículo mínimo.
        """
        while i // 2 > 0:
            # Accedemos a get_riesgo() para comparar las prioridades
            prioridad_hijo = self.listaMonticulo[i].get_riesgo()
            prioridad_padre = self.listaMonticulo[i // 2].get_riesgo()
            
            #Corrobora si el hijo es menor que el padre
            if prioridad_hijo < prioridad_padre:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            #Recorre todo el monticulo hasta llegar a 0
            i = i // 2

    def infiltAbajo(self, i):
        """
        Precondición:
        i debe ser un entero positivo.
        i debe corresponder a una posición válida del montículo.

        Postcondición:
        El subárbol cuya raíz se encuentra en i cumple la propiedad
        de montículo mínimo.
        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            prioridad_padre = self.listaMonticulo[i].get_riesgo()
            prioridad_hijo_min = self.listaMonticulo[hm].get_riesgo()
            
            if prioridad_padre > prioridad_hijo_min:
                self.listaMonticulo[i], self.listaMonticulo[hm] = self.listaMonticulo[hm], self.listaMonticulo[i]
            i = hm
    
    def insertar(self, k):
        """
        Precondición:
        k debe poseer el método get_riesgo().
        get_riesgo() debe devolver un valor comparable.

        Postcondición:
        El elemento es agregado al montículo.
        Se mantiene la propiedad de montículo mínimo.
        El tamaño del montículo aumenta en una unidad.

        Excepciones:
        TypeError si el elemento no posee el método get_riesgo().
        """
        if not hasattr(k, "get_riesgo"):
            raise TypeError("El elemento debe implementar get_riesgo()")
        self.listaMonticulo.append(k)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)    
        
        
    def eliminarMin(self):
        """
        Precondición:
        El montículo puede estar vacío o contener elementos.

        Postcondición:
        Devuelve el elemento con menor prioridad.
        Si el montículo no estaba vacío, el tamaño disminuye en una unidad.
        Se mantiene la propiedad de montículo mínimo.

        Retorna:
        El elemento de menor prioridad o None si el montículo está vacío.
        """
        #El monticulo empieza desde 1
        if self.tamanoActual == 0:
            return None
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] #Intercambia de lugar al nodo ultimo con el primero
        self.tamanoActual -= 1
        self.listaMonticulo.pop() #Elimina el primer ultimo nodo
        if self.tamanoActual > 0: 
            self.infiltAbajo(1) #Ordena el monticulo
        return valorSacado

    def construirMonticulo(self,unaLista):
        """
        Precondición:
        unaLista debe ser una lista.
        Todos sus elementos deben poseer el método get_riesgo().

        Postcondición:
        Se construye un montículo mínimo a partir de los elementos de la lista.
        El tamaño del montículo coincide con la cantidad de elementos recibidos.

        Excepciones:
        TypeError si unaLista no es una lista o contiene elementos inválidos.
        """
        if not isinstance(unaLista, list):
            raise TypeError("Se esperaba una lista")
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def __len__(self):       
        """
        Precondición:
        El montículo debe existir.

        Postcondición:
        Devuelve la cantidad de elementos almacenados.
        No modifica el montículo.
        """
        
        return self.tamanoActual
    
    def __iter__(self):
        """
        Precondición:
        El montículo debe existir.

        Postcondición:
        Permite recorrer todos los elementos almacenados
        sin modificar la estructura del montículo.

        Yields:
            dato: elemento siguiente de la lista.
        """
        for i in range(1, self.tamanoActual + 1):
            yield self.listaMonticulo[i]
    

    
    
