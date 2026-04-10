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
        if self.__tamanio == 0:
            self.__cabeza = item
            self.__cola = item
        else:
            cabeza_viejo = self.__cabeza
            self.__cabeza = item
            
    def agregar_al_final(self, item):
        pass

if __name__ == '__main__':
    item = "Ocupado"
    mi_lista = ListaDobleEnlazada()
    mi_lista.agregar_al_inicio(item)
    print(mi_lista.esta_vacia())
        
         
    