class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        # ATRIBUTOS DE ESTADO AGREGADOS (Para algoritmos de exploración y optimización)
        self.distancia = float('inf')  # Inicializado en infinito para Dijkstra/BEA
        self.predecesor = None
        self.color = 'blanco'          # blanco = no visitado, gris = visitando, negro = terminado
        self.descubrimiento = 0
        self.finalizacion = 0

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]
    
    # MÉTODOS MISING AGREGADOS (Getters y Setters de Estado)
    def asignarDistancia(self, d):
        self.distancia = d

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, p):
        self.predecesor = p

    def obtenerPredecesor(self):
        return self.predecesor

    def asignarColor(self, c):
        self.color = c

    def obtenerColor(self):
        return self.color

    def asignarDescubrimiento(self, t):
        self.descubrimiento = t

    def asignarFinalizacion(self, t):
        self.finalizacion = t


class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


def construirGrafo(archivoPalabras):
    d = {}
    g = Grafo()
    with open(archivoPalabras, 'r') as archivo:
        # crear baldes de palabras que se diferencian por una letra
        for linea in archivo:
            palabra = linea.strip()
            for i in range(len(palabra)):
                balde = palabra[:i] + '_' + palabra[i+1:]
                if balde in d:
                    d[balde].append(palabra)
                else:
                    d[balde] = [palabra]
    # agregar vértices y aristas para palabras en el mismo balde
    for balde in d.keys():
        for palabra1 in d[balde]:
            for palabra2 in d[balde]:
                if palabra1 != palabra2:
                    g.agregarArista(palabra1, palabra2)
    return g


class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)


class ColaDoble:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregarFrente(self, item):
        self.items.append(item)

    def agregarFinal(self, item):
        self.items.insert(0, item)

    def removerFrente(self):
        return self.items.pop()

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)


def bea(g, inicio):
    inicio.asignarDistancia(0)
    inicio.asignarPredecesor(None)
    colaVertices = Cola()
    colaVertices.agregar(inicio)
    while colaVertices.tamano() > 0:
        verticeActual = colaVertices.avanzar()
        for vecino in verticeActual.obtenerConexiones():
            if vecino.obtenerColor() == 'blanco':
                vecino.asignarColor('gris')
                vecino.asignarDistancia(verticeActual.obtenerDistancia() + 1)
                vecino.asignarPredecesor(verticeActual)
                colaVertices.agregar(vecino)
        verticeActual.asignarColor('negro')


def recorrer(y):
    x = y
    if x is None:
        print("El vértice no existe.")
        return
    while x.obtenerPredecesor():
        print(x.obtenerId())
        x = x.obtenerPredecesor()
    print(x.obtenerId())


def grafoDelCaballo(tamanoTablero):
    grafoCbllo = Grafo()
    for fil in range(tamanoTablero):
        for col in range(tamanoTablero):
            idNodo = pos_A_Id_Nodo(fil, col, tamanoTablero)
            posicionesNuevas = generarMovLegales(fil, col, tamanoTablero)
            for e in posicionesNuevas:
                nid = pos_A_Id_Nodo(e[0], e[1], tamanoTablero)
                grafoCbllo.agregarArista(idNodo, nid)
    return grafoCbllo


def pos_A_Id_Nodo(fila, columna, tamano_del_tablero):
    return (fila * tamano_del_tablero) + columna


def generarMovLegales(x, y, tamanoTablero):
    nuevosMovimientos = []
    desplazamientosEnL = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                          (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in desplazamientosEnL:
        nuevoX = x + i[0]
        nuevoY = y + i[1]
        if coordLegal(nuevoX, tamanoTablero) and coordLegal(nuevoY, tamanoTablero):
            nuevosMovimientos.append((nuevoX, nuevoY))
    return nuevosMovimientos


def coordLegal(x, tamanoTablero):
    return 0 <= x < tamanoTablero


def giraCaballo(n, ruta, u, limite):
    u.asignarColor('gris')
    ruta.append(u)
    if n < limite:
        listaVecinos = list(u.obtenerConexiones())
        i = 0
        hecho = False
        while i < len(listaVecinos) and not hecho:
            if listaVecinos[i].obtenerColor() == 'blanco':
                hecho = giraCaballo(n + 1, ruta, listaVecinos[i], limite)
            i = i + 1
        if not hecho:  # prepararse para retroceder
            ruta.pop()
            u.asignarColor('blanco')
    else:
        hecho = True
    return hecho


def ordenPorDisp(n):
    listaRes = []
    for v in n.obtenerConexiones():
        if v.obtenerColor() == 'blanco':
            c = 0
            for w in v.obtenerConexiones():
                if w.obtenerColor() == 'blanco':
                    c = c + 1
            listaRes.append((c, v))
    listaRes.sort(key=lambda x: x[0])
    return [y[1] for y in listaRes]


class ColaPrioridad:
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

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltrarArriba(self.tamanoActual)

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
        valorRetorno = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltrarAbajo(1)
        return valorRetorno

    def construirMonticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [[0]] + unaLista[:]
        while i > 0:
            self.infiltrarAbajo(i)
            i = i - 1

    def decrementarClave(self, val, nueva_clave):
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == val:
                self.listaMonticulo[i][0] = nueva_clave
                self.infiltrarArriba(i)
                break

    def estaVacia(self):
        return self.tamanoActual == 0


class grafoBEP(Grafo):
    def __init__(self):
        super().__init__()
        self.tiempo = 0

    def bep(self):
        for unVertice in self:
            unVertice.asignarColor('blanco')
            unVertice.asignarPredecesor(-1)
        for unVertice in self:
            if unVertice.obtenerColor() == 'blanco':
                self.visitabep(unVertice)

    def visitabep(self, verticeInicio):
        verticeInicio.asignarColor('gris')
        self.tiempo += 1
        verticeInicio.asignarDescubrimiento(self.tiempo)
        for siguienteVertice in verticeInicio.obtenerConexiones():
            if siguienteVertice.obtenerColor() == 'blanco':
                siguienteVertice.asignarPredecesor(verticeInicio)
                self.visitabep(siguienteVertice)
        verticeInicio.asignarColor('negro')
        self.tiempo += 1
        verticeInicio.asignarFinalizacion(self.tiempo)


def dijkstra(unGrafo, inicio):
    cp = ColaPrioridad()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
    while not cp.estaVacia():
        # CORRECCIÓN AQUÍ: Desempaquetamos la tupla [distancia, objeto_vertice]
        distanciaActual, verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() \
                    + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente, nuevaDistancia)


# =========================================================================
# LÓGICA DE PROCESAMIENTO Y ALGORITMO DE PRIM
# =========================================================================

def cargar_y_limpiar_grafo(nombre_archivo):
    """
    Lee el archivo solucionando las líneas cortadas y registros huérfanos.
    Construye un objeto Grafo con las conexiones dadas.
    """
    g = Grafo()
    con_ant = ""
    
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea == "Diosleguarde":
                continue # Descarta la línea incompleta y las vacías
            
            # Si la línea quedó cortada terminando en coma, la guardamos
            if linea.endswith(","):
                con_ant = linea
                continue
            
            # Si veníamos de una línea cortada, las unimos
            if con_ant:
                linea = con_ant + " " + linea
                con_ant = ""
            
            partes = [p.strip() for p in linea.split(',')]
            if len(partes) == 3:
                origen, destino, distancia_str = partes
                try:
                    distancia = int(distancia_str)
                    g.agregarArista(origen, destino, distancia)
                except ValueError:
                    continue
    return g


def ejecutar_prim(unGrafo, inicio):
    """
    Algoritmo de Prim adaptado para usar la estructura ColaPrioridad del alumno.
    """
    cp = ColaPrioridad()
    
    # Inicialización de todos los vértices
    for v in unGrafo:
        v.asignarDistancia(float('inf'))
        v.asignarPredecesor(None)
        v.asignarColor('blanco')
        
    inicio.asignarDistancia(0)
    
    # Construimos el montículo con el formato [prioridad, objeto]
    cp.construirMonticulo([[v.obtenerDistancia(), v] for v in unGrafo])
    
    while not cp.estaVacia():
        distActual, verticeActual = cp.eliminarMin()
        verticeActual.asignarColor('negro') # Entra oficialmente al árbol de expansión (MST)
        
        for vecino in verticeActual.obtenerConexiones():
            # Si el vecino no forma parte del MST aún
            if vecino.obtenerColor() == 'blanco':
                costoArista = verticeActual.obtenerPonderacion(vecino)
                if costoArista < vecino.obtenerDistancia():
                    vecino.asignarDistancia(costoArista)
                    vecino.asignarPredecesor(verticeActual)
                    cp.decrementarClave(vecino, costoArista)


# =========================================================================
# PROGRAMA PRINCIPAL (Generación de Reportes Solicitados)
# =========================================================================

if __name__ == "__main__":
    archivo_datos = "data/aldeas.txt"
    grafo_palomas = cargar_y_limpiar_grafo(archivo_datos)
    
    # Ejecutamos el algoritmo partiendo del palomar de William
    nodo_inicio = grafo_palomas.obtenerVertice("Peligros")
    ejecutar_prim(grafo_palomas, nodo_inicio)
    
    # Obtener y ordenar la lista de aldeas numéricamente y alfabéticamente
    lista_aldeas = sorted(list(grafo_palomas.obtenerVertices()))
    
    print("==================================================================")
    print(f" SOLICITUD 1: LISTA DE LAS {len(lista_aldeas)} ALDEAS EN ORDEN ALFABÉTICO")
    print("==================================================================")
    for i, nombre in enumerate(lista_aldeas, start=1):
        print(f"{i:2d}. {nombre}")
        
    print("\n==================================================================")
    print(" SOLICITUD 2: FLUJO ÓPTIMO DE DISTRIBUCIÓN (RECEPCIÓN Y RÉPLICAS)")
    print("==================================================================")
    
    for nombre in lista_aldeas:
        v = grafo_palomas.obtenerVertice(nombre)
        print(f"\n🏠 Aldea: {nombre.upper()}")
        
        # Bloque de recepción
        if nombre == "Peligros":
            print("   📥 Recepción : Sede central (William). Inicia la transmisión de la noticia.")
        else:
            pred = v.obtenerPredecesor()
            if pred:
                print(f"   📥 Recepción : Debe recibirla de '{pred.obtenerId()}' (Recorrido de {v.obtenerDistancia()} leguas).")
            else:
                print("   📥 Recepción : ¡Inalcanzable!")
                
        # Bloque de réplicas
        replicas = []
        for v_posible in grafo_palomas:
            if v_posible.obtenerPredecesor() == v:
                replicas.append(v_posible.obtenerId())
                
        if replicas:
            print(f"   📤 Réplicas  : Debe replicar y enviar el mensaje a: {', '.join(sorted(replicas))}")
        else:
            print("   📤 Réplicas  : No necesita enviar réplicas a ninguna vecina.")
            
    print("\n==================================================================")
    print(" SOLICITUD 3: TOTAL DE RECURSOS DEL ENVÍO (COSTO MÍNIMO DEL MST)")
    print("==================================================================")
    
    suma_total_leguas = 0
    for v in grafo_palomas:
        if v.obtenerId() != "Peligros" and v.obtenerDistancia() != float('inf'):
            suma_total_leguas += v.obtenerDistancia()
            
    print(f" Suma de todas las distancias recorridas por las palomas: {suma_total_leguas} leguas.")
    print("==================================================================")
    