class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None 

class ListaDobleEnlazada:
    
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0

    @property
    def cabeza(self):
        return self.__cabeza
    
    @property
    def cola(self):
        return self.__cola
    
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
    
    @cola.setter
    def cola(self,item):
        self.__cola = item
    
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
    
    def extraer(self, posicion):
        pass

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza

        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        
        return copia
    
    def invertir(self):
        pass

    def concatenar(self, Lista):
        pass


    def __len__(self):
        return self.__tamanio

    def __add__(self, Lista):
        pass

    def __iter__(self):
        pass

    