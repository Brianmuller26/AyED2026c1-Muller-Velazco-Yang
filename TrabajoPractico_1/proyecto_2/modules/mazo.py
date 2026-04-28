from modules.LDE import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass 

class Mazo:
    
    def __init__ (self):
        self.__mazo = ListaDobleEnlazada()
        self.__carta = Carta()
        self.__tamanio = 0

    def poner_carta_arriba(self, carta):
        self.__mazo.agregar_al_inicio(carta)
        self.__tamanio += 1
    
    def poner_carta_abajo(self, carta):
        self.__mazo.agregar_al_final(carta)
        self.__tamanio += 1

    def sacar_carta_arriba(self, mostrar = True):
        if self.__tamanio == 0:
            raise DequeEmptyError("Lista Vacia")
        else:
            self.__tamanio -= 1
            return self.__mazo.extraer(0)
        
    def __len__(self):
        return self.__tamanio