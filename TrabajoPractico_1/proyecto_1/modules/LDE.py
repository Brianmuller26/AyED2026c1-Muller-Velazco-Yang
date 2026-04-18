class Nodo:

    def __init__(self,dato):
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
        return self.__tamanio == 0

    @cabeza.setter
    def cabeza(self,dato):
        self.__cabeza = dato
    
    @cola.setter
    def cola(self,dato):
        self.__cola = dato
    
    def agregar_al_inicio(self, dato):
        
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, dato):
        
        nuevo_nodo = Nodo(dato)
        if self.cola is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__cola
            self.__cola.siguiente = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

if __name__ == '__main__':
    mi_lista = ListaDobleEnlazada()
    print("Vacía: ", mi_lista.esta_vacia())

    item = "Ocupado"
    
    mi_lista.agregar_al_inicio(item)
    print("Con ítem: ", mi_lista.esta_vacia())