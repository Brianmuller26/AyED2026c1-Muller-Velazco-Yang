class Vertice:
    def __init__(self, clave):
        """
        Precondición:
        clave debe ser un identificador válido de la aldea.

        Postcondición:
        Se crea un vértice sin conexiones.
        La distancia se inicializa en infinito.
        El predecesor queda en None.

        Excepciones:
        ValueError si clave es None.
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")
        self.id = clave
        self.conectadoA = {}          # Guarda los vecinos y la distancia a ellos
        self.distancia = float() # Leguas necesarias para conectarlo al árbol (empieza en infinito)
        self.predecesor = None        # De qué aldea vecina recibe la noticia
        self.color = 'blanco'         # 'blanco' = no visitado,     'negro' = ya integrado óptimamente

    def agregarVecino(self, vecino, ponderacion=0):
        """
        Precondición:
        vecino debe ser un objeto Vertice.
        ponderacion debe ser un número mayor o igual a 0.

        Postcondición:
        Se agrega una conexión hacia el vértice vecino
        con la ponderación indicada.

        Excepciones:
        TypeError si vecino no es un Vertice.
        ValueError si ponderacion es negativa.
        """

        if not isinstance(vecino, Vertice):
            raise TypeError("vecino debe ser un Vertice")

        if ponderacion < 0:
            raise ValueError("La ponderación no puede ser negativa")
        # Establece una ruta hacia una aldea vecina con su distancia en leguas
        self.conectadoA[vecino] = ponderacion

    def obtenerConexiones(self):
        """
        Precondición:
        El vértice debe existir.

        Postcondición:
        Devuelve una colección con todos los vértices vecinos conectados.
        No modifica el grafo.
        """
        # Devuelve las aldeas vecinas a las que puede enviar palomas
        return self.conectadoA.keys()

    def obtenerId(self):
        """
        Precondición:
        El vértice debe existir.

        Postcondición:
        Devuelve el identificador del vértice.
        """
        # Devuelve el nombre de la aldea
        return self.id

    def obtenerPonderacion(self, vecino):
        """
        Precondición:
        vecino debe estar conectado al vértice actual.

        Postcondición:
        Devuelve la ponderación de la arista entre ambos vértices.

        Excepciones:
        KeyError si el vecino no está conectado.
        """

        if vecino not in self.conectadoA:
            raise KeyError("El vecino no está conectado")
        # Devuelve la distancia exacta en leguas hacia un vecino particular
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        """
        Precondición:
        Ninguna.

        Postcondición:
        Se crea un grafo vacío sin vértices.
        """
        self.listaVertices = {} 
    
    def agregarVertice(self, clave):
        """
        Precondición:
        clave debe ser válida y no existir previamente en el grafo.

        Postcondición:
        Se agrega un nuevo vértice al grafo.

        Excepciones:
        ValueError si clave es None.
        """
        if clave is None:
            raise ValueError("La clave no puede ser None")

        if clave in self.listaVertices:
            raise ValueError("El vértice ya existe")
        # Crea una aldea en el mapa si aún no existía
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        """
        Precondición:
        n debe ser una clave válida.

        Postcondición:
        Devuelve el vértice asociado o None.

        Excepciones:
        ValueError si n es None.
        """

        if n is None:
            raise ValueError("La clave no puede ser None")
        # Busca una aldea por su nombre. Devuelve None si no existe
        return self.listaVertices.get(n)

    def agregarArista(self, de, a, costo=0):
        """
        Precondición:
        de y a deben ser claves válidas.
        costo debe ser mayor o igual a 0.

        Postcondición:
        Se agrega una arista desde 'de' hacia 'a'.

        Excepciones:
        ValueError si alguna clave es None
        o si costo es negativo.
        """

        if de is None or a is None:
            raise ValueError("Las claves no pueden ser None")

        if costo < 0:
            raise ValueError("El costo no puede ser negativo")
        # Crea la conexión entre dos aldeas con su distancia
        if de not in self.listaVertices:
            self.agregarVertice(de)

        if a not in self.listaVertices:
            self.agregarVertice(a)

        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        """
        Precondición:
        El grafo debe existir.

        Postcondición:
        Devuelve una colección con las claves de todos los vértices.
        No modifica el grafo.
        """
        # Devuelve los nombres de todas las aldeas registradas
        return self.listaVertices.keys()

    def __iter__(self):
        """
        Precondición:
        El grafo debe existir.

        Postcondición:
        Devuelve un iterador sobre los vértices del grafo.
        """
        return iter(self.listaVertices.values())

class ColaPrioridad:
    """Estructura de Montículo Mínimo que organiza las aldeas por menor distancia"""
    def __init__(self):
        self.listaMonticulo = [[0]]
        self.tamanoActual = 0

    def infiltrarArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def infiltrarAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            mc = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[mc][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[mc]
                self.listaMonticulo[mc] = tmp
            i = mc

    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        """
        Precondición:
        El montículo no debe estar vacío.

        Postcondición:
        Se elimina y devuelve el elemento mínimo.

        Excepciones:
        IndexError si el montículo está vacío.
        """

        if self.tamanoActual == 0:
            raise IndexError("El montículo está vacío")
        # Extrae de forma eficiente la aldea que se encuentra más cerca de la red actual
        valorRetorno = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltrarAbajo(1)
        return valorRetorno

    def construirMonticulo(self, unaLista):
        """
        Precondición:
        unaLista debe ser una lista válida.

        Postcondición:
        Los elementos quedan organizados
        como un montículo mínimo.

        Excepciones:
        TypeError si unaLista no es una lista.
        """

        if not isinstance(unaLista, list):
            raise TypeError("Se esperaba una lista")
        # Toma la lista inicial de aldeas y las estructura en forma de montículo
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [[0]] + unaLista[:]
        while i > 0:
            self.infiltrarAbajo(i)
            i = i - 1

    def decrementarClave(self, val, nueva_clave):
        """
        Precondición:
        val debe existir en el montículo.
        nueva_clave no debe ser None.

        Postcondición:
        Se actualiza la prioridad del elemento.

        Excepciones:
        ValueError si nueva_clave es inválida.
        """

        if nueva_clave is None:
            raise ValueError("La nueva clave no puede ser None")
        # Actualiza la distancia de una aldea cuando encontramos un camino más corto hacia ella
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == val:
                self.listaMonticulo[i][0] = nueva_clave
                self.infiltrarArriba(i)
                break

    def estaVacia(self):
        """
        Precondición:
        La cola de prioridad debe existir.

        Postcondición:
        Devuelve True si la cola está vacía.
        Devuelve False en caso contrario.
        """
        return self.tamanoActual == 0

def prim(g, inicio):
    """
    Precondición:
    g debe ser un grafo válido.
    inicio debe pertenecer al grafo.

    Postcondición:
    Se genera el árbol de expansión mínima.
    Cada vértice almacena su predecesor
    y la distancia mínima correspondiente.

    Excepciones:
    ValueError si g o inicio son None.
    """
    if g is None:
        raise ValueError("El grafo no puede ser None")

    if inicio is None:
        raise ValueError("El vértice inicial no puede ser None")

    if inicio not in g.listaVertices.values():
        raise ValueError("El vértice inicial no pertenece al grafo")
    cp = ColaPrioridad()
    for v in g:
        v.distancia = float('inf')
        v.predecesor = None
        v.color = 'blanco'   
    inicio.distancia = 0
    
    cp.construirMonticulo([[v.distancia, v] for v in g])
    
    while not cp.estaVacia():
        # Tomamos la aldea más accesible que no haya sido integrada todavía
        distActual, verticeActual = cp.eliminarMin()
        verticeActual.color = 'negro' # Se marca como integrada permanentemente a la red
        
        for vecino in verticeActual.obtenerConexiones():# Revisamos todos sus vecinos
            if vecino.color == 'blanco':
                costoArista = verticeActual.obtenerPonderacion(vecino)
                if costoArista < vecino.distancia:# Si es más corto llegar a este vecino desde la aldea actual que desde rutas previas
                    vecino.distancia = costoArista
                    vecino.predecesor = verticeActual # Guardamos el enlace de procedencia
                    cp.decrementarClave(vecino, costoArista)