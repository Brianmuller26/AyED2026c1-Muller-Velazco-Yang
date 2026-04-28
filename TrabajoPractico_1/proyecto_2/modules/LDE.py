class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__nodo = None
        self.__tamanio = 0

    @property
    def cabeza(self):
        return self.__cabeza
    
    @property
    def cola(self):
        return self.__cola
    
    @property
    def nodo(self):
        return self.__nodo
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    def esta_vacia(self):
        if self.__tamanio == 0:
            return True
        else:
            return False

    @cabeza.setter
    def cabeza(self,item):
        self.__cabeza = item
        self.anterior = None
        self.siguiente = None
    
    @cola.setter
    def cola(self,item):
        self.__cola = item
        self.anterior = None
        self.siguiente = None

    @nodo.setter
    def nodo(self,item,posicion):
        self.__nodo = item
        self.anterior = None
        self.siguiente = None
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def agregar_al_inicio(self, item):
        
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, item):
        
        nuevo_nodo = Nodo(item)
        if self.cola is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__cola
            self.__cola.siguiente = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

    def insertar(self, item, posicion):

        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        
        if posicion == 0:
            self.agregar_al_inicio(item)

        elif posicion == self.tamanio:
            self.agregar_al_final(item)
        
        else:
            nuevo_nodo = Nodo(item)
            actual = self.cabeza

            for _ in range(posicion):
                actual = actual.siguiente

            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo

            self.tamanio += 1
    
    def extraer(self, posicion = None): 

        if self.__cabeza == None and self.__cola == None:
            raise Exception("Lista Vacia")       
        
        if posicion == 0:
            dato = self.__cabeza.dato
            self.__cabeza = self.__cabeza.siguiente

            if self.__cabeza is not None:
                self.__cabeza.anterior = None
            
            else:
                self.__cola = None

            self.__tamanio -= 1    
            return dato

        if posicion is None or posicion == self.__tamanio - 1 or posicion == -1:

            posicion == self.__tamanio - 1
            dato = self.__cola.dato
            self.__cola = self.__cola.anterior

            if self.__cola is not None:
                self.__cola.siguiente = None
                
            else:
                self.__cabeza = None
                
            self.__tamanio -= 1    
            return dato 

        
        if posicion != 0 and posicion != self.__tamanio:
            
            actual = self.cabeza
            
            for _ in range(posicion):
                actual = actual.siguiente
                dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

            self.__tamanio -= 1
            
            return dato

        if posicion < 0 or posicion > self.__tamanio:
            raise Exception("Posición inválida")
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza

        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        
        return copia
    
    def invertir(self):

        actual = self.__cabeza

        while actual is not None:

            actual.siguiente, actual.anterior = (
                actual.anterior,
                actual.siguiente
            )

            actual = actual.anterior

        # Intercambiar cabeza y cola
        self.__cabeza, self.__cola = self.__cola, self.__cabeza

    def concatenar(self, Lista):
        
        if Lista.tamanio == 0:
            return self
        
        actual = Lista.cabeza

        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente

        return self
        
    def __len__(self):
        return self.__tamanio

    def __add__(self, Lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(Lista)
        return nueva_lista

    def __iter__(self):
        
        actual = self.__cabeza
        for _ in range(self.__tamanio):
            
            yield actual.dato
            actual = actual.siguiente      