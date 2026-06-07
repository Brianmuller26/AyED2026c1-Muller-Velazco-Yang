class NodoArbol:
    def __init__(self, clave, valor, izquierdo = None, derecho = None, padre = None):
        """
        Precondición:

        clave debe ser comparable con otras claves del árbol.
        valor puede ser cualquier dato.
        Los parámetros izquierdo, derecho y padre deben ser nodos válidos o None.
        
        Postcondición:

        Se crea un nodo con la clave y valor indicados.
        El factor de equilibrio queda inicializado en 0.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        """
        Precondición:

        El nodo debe existir.

        Postcondición:

        Devuelve el hijo izquierdo si existe, o None en caso contrario.
        """
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        """
        Precondición:

        El nodo debe existir.

        Postcondición:

        Devuelve el hijo derecho si existe, o None en caso contrario.
        """
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        """
        Precondición:
        El nodo debe pertenecer a un árbol.

        Postcondición:
        Devuelve True si el nodo es hijo izquierdo de su padre.
        Devuelve False en caso contrario.
        """
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        """
        Precondición:
        El nodo debe pertenecer a un árbol.

        Postcondición:
        Devuelve True si el nodo es hijo derecho de su padre.
        Devuelve False en caso contrario.
        """
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        """
        Precondición:
        El nodo debe existir.

        Postcondición:
        Devuelve True si el nodo no posee padre.
        Devuelve False en caso contrario.
        """
        return not self.padre

    def esHoja(self):
        """
        Precondición:

        El nodo debe existir.

        Postcondición:

        Devuelve True si el nodo no tiene hijos.
        Devuelve False en caso contrario.
        """
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        """
        Precondición:

        El nodo debe existir.

        Postcondición:

        Devuelve True si posee al menos un hijo.
        """
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        """
        Precondición:

        El nodo debe existir.

        Postcondición:

        Devuelve True si posee hijo izquierdo y derecho.
        """
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        """
        Precondición:

        Los parámetros deben ser válidos.
        hizq y hder deben ser nodos o None.

        Postcondición:

        Actualiza la información almacenada en el nodo.
        Reasigna correctamente los padres de los hijos.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ArbolBinarioBusqueda:
    """
    Precondición:

    Ninguna.

    Postcondición:

    Se crea un árbol vacío.
    """

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        """
        Precondición:
        El árbol debe existir.

        Postcondición:
        Devuelve la cantidad de nodos almacenados en el árbol.
        No modifica la estructura del árbol.
        """
        return self.tamano

    def __len__(self):
        """
        Precondición:

        El árbol debe existir.

        Postcondición:

        Devuelve la cantidad de nodos almacenados en el árbol.
        No modifica la estructura del árbol.
        """
        return self.tamano

    def agregar(self, clave, valor):
        """
        Precondición:
        La clave debe ser comparable con las demás claves del árbol.

        Postcondición:
        Se inserta un nuevo nodo respetando la propiedad
        de árbol binario de búsqueda.
        El tamaño del árbol aumenta en una unidad.

        Excepciones:
        ValueError si la clave es None.
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        """
        Precondición:
        nodoActual debe pertenecer al árbol.
        La clave debe ser comparable con las demás claves.

        Postcondición:
        Se inserta un nuevo nodo respetando la propiedad
        de árbol binario de búsqueda.

        Excepciones:
        ValueError si nodoActual o clave son None.
        """

        if nodoActual is None:
            raise ValueError("El nodo actual no puede ser None")

        if clave is None:
            raise ValueError("La clave no puede ser None")

        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        """
        Precondición:
        La clave debe ser comparable con las demás claves del árbol.

        Postcondición:
        Se inserta un nuevo elemento utilizando la clave y el valor recibidos.
        El tamaño del árbol aumenta en una unidad.
        """
        self.agregar(c, v)

    def obtener(self, clave):
        """
        Precondición:        
        La clave debe ser comparable.

        Postcondición:
        Devuelve el valor asociado a la clave si existe.

        Excepciones:
        Devuelve None si la clave no se encuentra.
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")
        
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                    return res.cargaUtil
            else:
                    return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        """
        Precondición:
        nodoActual debe ser un nodo válido o None.

        Postcondición:
        Devuelve el nodo que contiene la clave buscada o None.
        """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        """
        Precondición:
        La clave debe ser comparable con las claves almacenadas.

        Postcondición:
        Devuelve el valor asociado a la clave indicada.
        Devuelve None si la clave no existe.
        """
        return self.obtener(clave)

    def __contains__(self, clave):
        """
        Precondición:
        La clave debe ser comparable con las claves almacenadas.

        Postcondición:
        Devuelve True si la clave pertenece al árbol.
        Devuelve False en caso contrario.

        Excepciones:
        Devuelve None si la clave no se encuentra.
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False

    def eliminar(self, clave):
        """
        Precondición:

        La clave debe existir en el árbol.

        Postcondición:

        El nodo correspondiente es eliminado.
        El tamaño del árbol disminuye en una unidad.
        Se mantiene la propiedad de ABB.
        """
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        """
        Precondición:
        La clave debe existir en el árbol.

        Postcondición:
        El nodo asociado a la clave es eliminado.
        El tamaño del árbol disminuye en una unidad.
        """
        self.eliminar(clave)

    def empalmar(self):
        """
        Precondición:
        El nodo debe pertenecer al árbol y tener cero o un hijo.

        Postcondición:
        El nodo es desconectado del árbol manteniendo correctamente los enlaces entre padre e hijos.
        La estructura del árbol continúa siendo válida.
        """
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                    if self.esHijoIzquierdo():
                        self.padre.hijoIzquierdo = self.hijoIzquierdo
                    else:
                        self.padre.hijoDerecho = self.hijoIzquierdo
                    self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                    self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
        """
        Precondición:

        El nodo debe pertenecer al árbol.

        Postcondición:

        Devuelve el sucesor in-order del nodo.
        Devuelve None si no existe sucesor.
        """
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        """
        Precondición:

        El subárbol no debe estar vacío.

        Postcondición:

        Devuelve el nodo con la menor clave del subárbol.
        """
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def remover(self, nodoActual):
        """
        Precondición:

        nodoActual debe pertenecer al árbol.

        Postcondición:

        El nodo es eliminado correctamente.
        La estructura del árbol sigue siendo válida.
        """
        if nodoActual.esHoja(): #hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos(): #interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)
        
class AVL(ArbolBinarioBusqueda):
    """Implementación de un Árbol AVL."""
    def _agregar(self, clave, valor, nodoActual):
        """
        Precondición:
        nodoActual debe pertenecer al árbol AVL.
        La clave debe ser comparable con las demás claves.

        Postcondición:
        Se inserta un nuevo nodo respetando las propiedades del árbol AVL.
        Se actualizan los factores de equilibrio necesarios.
        """
        if clave < nodoActual.clave:
            if nodoActual.hijoIzquierdo:
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.hijoDerecho:
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self, nodo):
        """
        Precondición:
        nodo debe pertenecer al árbol AVL.

        Postcondición:
        Se actualizan los factores de equilibrio.
        Si existe un desbalance se reequilibra el árbol.

        Excepciones:
        ValueError si nodo es None.
        """
        if nodo is None:
            raise ValueError("El nodo no puede ser None")
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            else:
                nodo.padre.factorEquilibrio -= 1
            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)
                    
    def rotarIzquierda(self, rotRaiz):
        """
        Precondición:
        rotRaiz debe existir y tener hijo derecho.

        Postcondición:
        El subárbol queda rotado hacia la izquierda.
        Se conserva la propiedad AVL.

        Excepciones:
        ValueError si no existe la raíz o no tiene hijo derecho.
        """

        if rotRaiz is None:
            raise ValueError("La raíz de rotación no puede ser None")

        if rotRaiz.hijoDerecho is None:
            raise ValueError("La rotación izquierda requiere un hijo derecho")
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        # Ajuste de factores de equilibrio simplificado para el ejercicio
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)

    def rotarDerecha(self, rotRaiz):
        """
        Precondición:
        rotRaiz debe existir y tener hijo izquierdo.

        Postcondición:
        El subárbol queda rotado hacia la derecha.
        Se conserva la propiedad AVL.

        Excepciones:
        ValueError si no existe la raíz o no tiene hijo izquierdo.
        """
        if rotRaiz is None:
            raise ValueError("La raíz de rotación no puede ser None")

        if rotRaiz.hijoIzquierdo is None:
            raise ValueError("La rotación derecha requiere un hijo izquierdo")
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                    rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def reequilibrar(self, nodo):
        """
        Precondición:
        nodo debe pertenecer al árbol AVL.

        Postcondición
        El subárbol queda balanceado mediante
        las rotaciones necesarias.

        Excepciones:
        ValueError si nodo es None.
        """
        if nodo is None:
            raise ValueError("El nodo no puede ser None")
        if nodo.factorEquilibrio < 0:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
                else:
                    self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
                else:
                    self.rotarDerecha(nodo)




def imprimir_estructura(nodo, nivel=0, prefijo="Raíz: "):
        """
        Precondición:

        nodo debe ser un nodo válido o None.

        Postcondición:

        Se muestra por pantalla la estructura jerárquica del árbol.
        No modifica el árbol.
        """
        """Imprime el árbol de costado para ver su forma jerárquica."""
        if nodo is not None:
            imprimir_estructura(nodo.hijoDerecho, nivel + 1, "Der: ")
            print(" " * (nivel * 4) + prefijo + str(nodo.clave) + f" [FE: {nodo.factorEquilibrio}]")
            imprimir_estructura(nodo.hijoIzquierdo, nivel + 1, "Izq: ")

if __name__ == "__main__":
    # """Prueba del factor de equilibrio y de rotación."""
    # lista = [1,2,4,6,8,9,32,89,23]
    # arbol = AVL()

    # Crear el árbol AVL
    arbol_test = AVL()

    print("--- Insertando el número 30 ---")
    arbol_test.agregar(30, "Valor 30")
    print("RAIZ:", arbol_test.raiz.factorEquilibrio)
    print("\n" + "-"*30)

    print("--- Insertando el número 20 ---")
    arbol_test.agregar(20, "Valor 20")
    
    print("\n" + "-"*30)

    print("--- Insertando el número 10 (Debería provocar una Rotación Simple a la Derecha) ---")
    arbol_test.agregar(10, "Valor 10")
    
    print("\n" + "-"*30)

    # print("--- Insertando el número 40 ---")
    # arbol_test.agregar(40, "Valor 40")
 
    # print("\n" + "-"*30)

    # print("--- Insertando el número 50 (Debería provocar una Rotación Simple a la Izquierda) ---")
    # arbol_test.agregar(50, "Valor 50")

        