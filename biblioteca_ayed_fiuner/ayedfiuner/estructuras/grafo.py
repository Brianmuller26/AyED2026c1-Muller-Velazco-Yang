class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}          # Guarda los vecinos y la distancia a ellos
        self.distancia = float() # Leguas necesarias para conectarlo al árbol (empieza en infinito)
        self.predecesor = None        # De qué aldea vecina recibe la noticia
        self.color = 'blanco'         # 'blanco' = no visitado,     'negro' = ya integrado óptimamente

    def agregarVecino(self, vecino, ponderacion=0):
        # Establece una ruta hacia una aldea vecina con su distancia en leguas
        self.conectadoA[vecino] = ponderacion

    def obtenerConexiones(self):
        # Devuelve las aldeas vecinas a las que puede enviar palomas
        return self.conectadoA.keys()

    def obtenerId(self):
        # Devuelve el nombre de la aldea
        return self.id

    def obtenerPonderacion(self, vecino):
        # Devuelve la distancia exacta en leguas hacia un vecino particular
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        self.listaVertices = {} 
    
    def agregarVertice(self, clave):
        # Crea una aldea en el mapa si aún no existía
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        # Busca una aldea por su nombre. Devuelve None si no existe
        return self.listaVertices.get(n)

    def agregarArista(self, de, a, costo=0):
        # Crea la conexión entre dos aldeas con su distancia
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        # Devuelve los nombres de todas las aldeas registradas
        return self.listaVertices.keys()

    def __iter__(self):
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
        # Extrae de forma eficiente la aldea que se encuentra más cerca de la red actual
        valorRetorno = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltrarAbajo(1)
        return valorRetorno

    def construirMonticulo(self, unaLista):
        # Toma la lista inicial de aldeas y las estructura en forma de montículo
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [[0]] + unaLista[:]
        while i > 0:
            self.infiltrarAbajo(i)
            i = i - 1

    def decrementarClave(self, val, nueva_clave):
        # Actualiza la distancia de una aldea cuando encontramos un camino más corto hacia ella
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == val:
                self.listaMonticulo[i][0] = nueva_clave
                self.infiltrarArriba(i)
                break

    def estaVacia(self):
        return self.tamanoActual == 0

def prim(g, inicio):
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