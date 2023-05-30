from modulos.Grafo import *
            
if __name__ == "__main__":
    """Se crea un objeto apartir de la clase Grafo"""
    g = Grafo()

    """Se agregan cada uno de los vertices al grafo"""
    g.agregar_vertice(Vertices)

    "Se agregan las aritas con su peso correspondiente"
    g.agregar_arista(Aristas)

    "Se dibuja el grafo con las vertices y sus aristas"
    g.dibujar_grafo()

    """Solicitamos al usuario agregar el vertice/nodo de origen"""
    v_origen = input("Ingrese el vertice de origen: ")  

    """Soliciatamos al usuario agregar el vertice/nodo de destino"""
    v_destino = input("Ingrese el vertice de destino: ")

    """Obtenemos el id del vertice de origen"""
    vertice_origen = g.obtener_vertice(v_origen)

    """Obtenemos el id del vertice de destino"""
    vertice_destino = g.obtener_vertice(v_destino)

    """Calculamos el Best Shortest Path apartir del vertice origen y el grafo"""
    BSP(g, vertice_origen.obtener_id())

    """La lista path va contener como resultado el camino mas corto"""
    path = []

    """Obtenemos el camino mas corto en base al vertice de destino"""
    resultado = shortest_path(vertice_destino, path)
    resultado.append(vertice_origen.obtener_id())
    print(resultado[::-1])