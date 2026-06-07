from ayedfiuner.estructuras.grafo import Grafo, prim

def cargar_y_limpiar_grafo(nombre_archivo):
    g = Grafo()
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
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
    archivo_datos = "data/aldeas.txt" 
    grafo_palomas = cargar_y_limpiar_grafo(archivo_datos)
    
    nodo_inicio = grafo_palomas.obtenerVertice("Peligros")
    prim(grafo_palomas, nodo_inicio)

    lista_aldeas = sorted(list(grafo_palomas.obtenerVertices()))
    
    print(f" Lista de las {len(lista_aldeas)} aldeas")
    for i, nombre in enumerate(lista_aldeas, start=1):
        print(f"{i:2d}. {nombre}")
        
    print("Distribución eficiente de la noticia ")
    for nombre in lista_aldeas:
        v = grafo_palomas.obtenerVertice(nombre)
        print(f"\nAldea: {nombre.upper()}")

        # Bloque de Recepción
        if nombre == "Peligros":
            print("Recepción : Palomas Williams. Inicia el envío.")
        else:
            pred = v.predecesor
            if pred:
                print(f"Recepción : '{pred.obtenerId()}', la distancia fue de {v.distancia} leguas.")
            else:
                print("Recepción: Sin receptor")
                
        # Bloque de Réplicas (Buscamos qué aldeas tienen a 'v' como su predecesor)
        replicas = []
        for v_posible in grafo_palomas:
            if v_posible.predecesor == v:
                replicas.append(v_posible.obtenerId())
                
        if replicas:
            print(f"Debe replicar y enviar el mensaje a: {', '.join(sorted(replicas))}")
        else:
            print("Fin de la ruta para esta paloma.")
            
    print(" Total de lo recorrido")
    suma_total_leguas = 0
    for v in grafo_palomas:
        # Sumamos la distancia de entrada de todas las aldeas, exceptuando la inicial
        if v.obtenerId() != "Peligros" and v.distancia != float('inf'):
            suma_total_leguas += v.distancia          
    print(f"\nSuma de todas las distancias recorridas por las palomas: {suma_total_leguas} leguas.")
  