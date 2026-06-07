from ayedfiuner.estructuras.grafo import Grafo, prim

def cargar_y_limpiar_grafo(nombre_archivo):
    """Lee el archivo solucionando las líneas cortadas y registros huérfanos."""
    g = Grafo()
    con_ant = ""
    
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            # Saltamos líneas vacías o la palabra suelta 'Diosleguarde'
            if not linea or linea == "Diosleguarde":
                continue 
            
            # Si la línea termina en coma, significa que el registro quedó cortado
            if linea.endswith(","):
                con_ant = linea
                continue
            
            # Si veníamos de una línea cortada, la unimos con la actual
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


if __name__ == "__main__":
    # Ajusta el nombre o ruta del archivo de texto si es necesario
    archivo_datos = "data/aldeas.txt" 
    grafo_palomas = cargar_y_limpiar_grafo(archivo_datos)
    
    # Buscamos el nodo de origen e iniciamos el algoritmo
    nodo_inicio = grafo_palomas.obtenerVertice("Peligros")
    prim(grafo_palomas, nodo_inicio)
    
    # Extraemos y ordenamos alfabéticamente los nombres de las aldeas
    lista_aldeas = sorted(list(grafo_palomas.obtenerVertices()))
    
    # -----------------------------------------------------------------
    # SOLICITUD 1: Mostrar la lista de aldeas en orden alfabético
    # -----------------------------------------------------------------
    print("==================================================================")
    print(f" SOLICITUD 1: LISTA DE LAS {len(lista_aldeas)} ALDEAS EN ORDEN ALFABÉTICO")
    print("==================================================================")
    for i, nombre in enumerate(lista_aldeas, start=1):
        print(f"{i:2d}. {nombre}")
        
    # -----------------------------------------------------------------
    # SOLICITUD 2: Flujo óptimo de mensajes (De quién recibe y a quién replica)
    # -----------------------------------------------------------------
    print("\n==================================================================")
    print(" SOLICITUD 2: FLUJO ÓPTIMO DE DISTRIBUCIÓN (RECEPCIÓN Y RÉPLICAS)")
    print("==================================================================")
    
    for nombre in lista_aldeas:
        v = grafo_palomas.obtenerVertice(nombre)
        print(f"\n🏠 Aldea: {nombre.upper()}")
        
        # Bloque de Recepción
        if nombre == "Peligros":
            print("   📥 Recepción : Sede Central (Palomar de William). Inicia el envío.")
        else:
            pred = v.predecesor
            if pred:
                print(f"   📥 Recepción : Debe recibirla de '{pred.obtenerId()}' (Vuelo de {v.distancia} leguas).")
            else:
                print("   📥 Recepción : ¡Inalcanzable!")
                
        # Bloque de Réplicas (Buscamos qué aldeas tienen a 'v' como su predecesor)
        replicas = []
        for v_posible in grafo_palomas:
            if v_posible.predecesor == v:
                replicas.append(v_posible.obtenerId())
                
        if replicas:
            print(f"   📤 Réplicas  : Debe replicar y enviar el mensaje a: {', '.join(sorted(replicas))}")
        else:
            print("   📤 Réplicas  : No necesita enviar réplicas (Fin de la ruta para esta paloma).")
            
    # -----------------------------------------------------------------
    # SOLICITUD 3: Suma total de las distancias recorridas
    # -----------------------------------------------------------------
    print("\n==================================================================")
    print(" SOLICITUD 3: TOTAL DE RECURSOS UTILIZADOS (SUMA DE LEGUAS)")
    print("==================================================================")
    
    suma_total_leguas = 0
    for v in grafo_palomas:
        # Sumamos la distancia de entrada de todas las aldeas, exceptuando la inicial
        if v.obtenerId() != "Peligros" and v.distancia != float('inf'):
            suma_total_leguas += v.distancia
            
    print(f" Suma de todas las distancias recorridas por las palomas: {suma_total_leguas} leguas.")
    print("==================================================================")