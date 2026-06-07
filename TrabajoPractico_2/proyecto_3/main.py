from ayedfiuner.estructuras.grafo import Grafo, ColaPrioridad

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