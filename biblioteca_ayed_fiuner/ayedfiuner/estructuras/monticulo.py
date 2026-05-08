class MonticuloBinario:
    
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0   

    def infiltArriba(self, i):
        while i // 2 > 0:
            # Accedemos a get_riesgo() para comparar las prioridades
            prioridad_hijo = self.listaMonticulo[i].get_riesgo()
            prioridad_padre = self.listaMonticulo[i // 2].get_riesgo()
            
            if prioridad_hijo < prioridad_padre:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = \
                    self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2
    
    
    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)    
    
    
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            prioridad_padre = self.listaMonticulo[i].get_riesgo()
            prioridad_hijo_min = self.listaMonticulo[hm].get_riesgo()
            
            if prioridad_padre > prioridad_hijo_min:
                self.listaMonticulo[i], self.listaMonticulo[hm] = \
                    self.listaMonticulo[hm], self.listaMonticulo[i]
            i = hm


    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            # Comparamos riesgos de los dos hijos
            if self.listaMonticulo[i*2].get_riesgo() < self.listaMonticulo[i*2+1].get_riesgo():
                return i * 2
            else:
                return i * 2 + 1
        
    def eliminarMin(self):
        if self.tamanoActual == 0:
            return None
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual -= 1
        self.listaMonticulo.pop()
        if self.tamanoActual > 0:
            self.infiltAbajo(1)
        return valorSacado



    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def __len__(self):
        """
        Devuelve la cantidad de elementos de la lista.

        Returns:
            int: tamaño de la lista.
        """
        return self.tamanoActual
    
    def __iter__(self):
        """
        Permite recorrer los elementos de la lista.

        Yields:
            dato: elemento siguiente de la lista.
        """
        for i in range(1, self.tamanoActual + 1):
            yield self.listaMonticulo[i]
    

    
    
