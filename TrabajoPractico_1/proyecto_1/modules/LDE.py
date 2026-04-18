class Nodo:

    def __init__(self,item):
        self.__item = item
        self.__siguiente = None
        self.__anterior = None 

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
        if self.__tamanio is None:
            return True

    @cabeza.setter
    def cabeza(self,item):
        self.__cabeza=item
    
    @cola.setter
    def cola(self,item):
        self.__cola=item
    
    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.__siguiente = self.__cabeza
            self.cabeza.__anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.cola is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.__anterior = self.__cola
            self.cola.__anterior = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

if __name__ == '__main__':
    item = "Ocupado"
    mi_lista = ListaDobleEnlazada()
    mi_lista.agregar_al_inicio(item)
    print(mi_lista.esta_vacia())