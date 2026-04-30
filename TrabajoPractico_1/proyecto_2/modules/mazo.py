from ayedfiuner.estructuras.LDE import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass 

class Mazo:
    
    def __init__ (self):
        """
        Inicializa un mazo vacío.

        Post:
            - el mazo queda vacío
            - el tamaño inicial es 0
        """
        self.__mazo = ListaDobleEnlazada()
        self.__tamanio = 0

    def poner_carta_arriba(self, carta):
        """
        Agrega una carta en la parte superior del mazo.

        Args:
            carta (Carta): carta a insertar.

        Pre:
            - carta debe ser una instancia de Carta

        Post:
            - la carta queda ubicada al inicio del mazo
            - el tamaño del mazo aumenta en 1
        """
        self.__mazo.agregar_al_inicio(carta)
        self.__tamanio += 1
    
    def poner_carta_abajo(self, carta):
        """
        Agrega una carta en la parte inferior del mazo.

        Args:
            carta (Carta): carta a insertar.

        Pre:
            - carta debe ser una instancia de Carta

        Post:
            - la carta queda ubicada al final del mazo
            - el tamaño del mazo aumenta en 1
        """
        self.__mazo.agregar_al_final(carta)
        self.__tamanio += 1

    def sacar_carta_arriba(self, mostrar = True):
        """
        Extrae la carta ubicada en la parte superior del mazo.

        Args:
            mostrar (bool): indica si la carta extraída debe
            quedar visible.

        Pre:
            - el mazo no debe estar vacío

        Post:
            - se elimina una carta del inicio del mazo
            - el tamaño del mazo disminuye en 1
            - si mostrar es True, la carta queda visible

        Returns:
            Carta: carta extraída del mazo.

        Raises:
            DequeEmptyError: si el mazo está vacío.
        """
        if self.__tamanio == 0:
            raise DequeEmptyError("Lista Vacia")
        else:
            if mostrar == True:
                carta = self.__mazo.extraer(0)
                carta.visible = True
            self.__tamanio -= 1
            return carta
        
    def __len__(self):
        """
        Devuelve la cantidad de cartas del mazo.

        Returns:
            int: cantidad de cartas almacenadas.
        """
        return self.__tamanio