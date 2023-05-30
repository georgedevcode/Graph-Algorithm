import sys

class Vertice:
    '''
Clase Vertice representa cada vertice del grafo.

Datos:
    id : identificador del nodo/vertice
    adyacente : vecinoes adyacente al nodo/vertice
    distancia : distancia/peso
    nodo_visitado : si el nodo ha sido visitado
    nodo_previo : nodo previo al nodo actual

Metodos:
    agregar_vecino
    obtener_conexiones
    obtener_id
    obtener_peso
    set_distancia
    obtener_distancia
    set_nodo_previo
    set_nodo_visitado
'''
    def __init__(self, nodo):
        self.id = nodo
        self.adyacente = {}  
        self.distancia = sys.maxsize
        self.nodo_visitado = False  
        self.nodo_previo = None

    def agregar_vecino(self, vecino, peso=0):
        self.adyacente[vecino] = peso
    
    def obtener_conexiones(self):
        return self.adyacente.keys()
    
    def obtener_id(self):
        return self.id

    def obtener_peso(self, vecino):
        return self.adyacente[vecino]
    
    def set_distancia(self, distancia):
        self.distancia = distancia
    
    def obtener_distancia(self):
        return self.distancia
    
    def set_nodo_previo(self, nodo_previo):
        self.nodo_previo = nodo_previo
    
    def set_nodo_visitado(self):
        self.nodo_visitado = True

    def __str__(self):
        return f"{str(self.id)} adyacente {str([nodo.id for nodo in self.adyacente])}"
    

class Grafo:
    '''
        Clase Grafo representa el grafo con todos sus vertices/nodos

        Datos:
            vertices : lista de vertices que componen el grafo
            numero_vertices : cantidad de vertices en el grafo
        
        Metodos:
            agregar_vertice
            obtener_vertice
            agregar_arista
            obtener_vertices
            set_nodo_previo
            dibujar_grafo
    '''
    def __init__(self):
        self.vertices = {}
        self.numero_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())
    
    def agregar_vertice(self, nodos):
        for nodo in nodos:
            self.numero_vertices = self.numero_vertices + 1
            nuevo_vertice = Vertice(nodo)
            self.vertices[nodo] = nuevo_vertice
        return nuevo_vertice
    
    def obtener_vertice(self, nodo):
        if nodo in self.vertices:
            return self.vertices[nodo]
        else:
            return print(f"{nodo} no fue encontrado en el grafo")
        
    def agregar_arista(self, aristas):
        for arista in aristas:
            nodo_primario = arista["nodo_primario"]
            nodo_secundario = arista["nodo_secundario"]
            peso = arista["peso"]

            if nodo_primario not in self.vertices:
                self.agregar_vertice(nodo_primario)
            
            if nodo_secundario not in self.vertices:
                self.agregar_vertice(nodo_secundario)
        
            self.vertices[nodo_primario].agregar_vecino(self.vertices[nodo_secundario], peso)
            self.vertices[nodo_secundario].agregar_vecino(self.vertices[nodo_primario], peso)
    
    def obtener_vertices(self):
        return self.vertices.keys()

    def set_nodo_previo(self, nodo_actual):
        self.nodo_previo = nodo_actual

    def dibujar_grafo(self):
            vertices = self.vertices.values()
            for vertice in vertices:
                conexiones = vertice.obtener_conexiones()
                for conexion in conexiones:
                    vertice_primario = vertice.obtener_id()
                    vertice_secundario = conexion.obtener_id()
                    print(f"({vertice_primario} - {vertice_secundario} - {vertice.obtener_peso(conexion)})")

def shortest_path(vertice_destino, path):
    '''Retorna el camino mas corto en base al nodo/vertice destino

    Argumentos:
        vertice_destino 
        path 

    Retorna:
        path
    '''
    if vertice_destino.nodo_previo:
        path.append(vertice_destino.obtener_id())
        shortest_path(vertice_destino.nodo_previo, path)
    return path
   

def BSP(grafo, vertice):
    '''Funcion Best Shortest Path usando el algoritmo de Dijkstra
    Args:
        grafo : grafo compuesto por vertices
        vertice : vertice de origen
    '''
    vertice_inicio = grafo.obtener_vertice(vertice)
    vertice_inicio.set_distancia(0)

    nodos_no_visitados = []
    for vertice in grafo:
        if not vertice.nodo_visitado:
            nodos_no_visitados.append(vertice)

    while len(nodos_no_visitados):
            nodo_actual = nodos_no_visitados[0]
            nodo_actual.set_nodo_visitado()
            for siguiente_nodo in nodo_actual.adyacente:
                nueva_distancia = nodo_actual.obtener_distancia() + nodo_actual.obtener_peso(siguiente_nodo)
                if nueva_distancia < siguiente_nodo.obtener_distancia():
                    siguiente_nodo.set_distancia(nueva_distancia)
                    siguiente_nodo.set_nodo_previo(nodo_actual)
                    print(f"Actualizando - Nodo actual: {str(nodo_actual.obtener_id())} - Nodo vecino: {str(siguiente_nodo.obtener_id())} - distancia: {str(siguiente_nodo.obtener_distancia())}")
                else:
                    print(f"Sin actualizar - Nodo actual: {str(nodo_actual.obtener_id())} - Nodo vecino: {str(siguiente_nodo.obtener_id())} - distancia: {str(siguiente_nodo.obtener_distancia())}")           
            if nodo_actual.nodo_visitado:
                nodos_no_visitados.remove(nodo_actual)
                print(len(nodos_no_visitados))

Vertices = ["Q"
        ,"U",
        "I",
         "O", 
         "Y",
         "JJ",
         "A", 
         "S", 
         "F", 
         "P", 
         "J", 
         "K", 
         "OZ", 
         "J", 
         "H", 
         "L", 
         "Z", 
         "X", 
         "G", 
         "D", 
         "M", 
         "C", 
         "V", 
         "B", 
         "N", 
         "CC", 
         "HH", 
         "NN", 
         "MM", 
         "SS", 
         "DD", 
         "FF", 
         "BB", 
         "GG", 
         "YU", 
         "IO", 
         "PA", 
         "LL", 
         "QE", 
         "RT",
         "KL",
         "ZX",
         "SD",
         "FG",
         "HJ",
         "FD",
         "TR",
         "CV",
         "BN",
         "NM",
         "LK",
         "JH",
         "GF",
         "SA",
         "RC",
         "EW",
         "YT",
         "IU",
         "OI",
         "PO",
         "ON",
         "TM",
         "EC",
         "RV",
         "UB",
         "TN",
         "TB"]

Aristas = [
            {"nodo_primario": "Q",
            "nodo_secundario": "U",
            "peso":6},
            {"nodo_primario":"Q",
            "nodo_secundario":"Y",
            "peso":5},
            {"nodo_primario":"Q",
            "nodo_secundario":"H",
            "peso":9},
            {"nodo_primario":"Y",
            "nodo_secundario":"Q",
            "peso":5},
            {"nodo_primario":"Y",
            "nodo_secundario":"A",
            "peso":8},
            {"nodo_primario":"Y",
            "nodo_secundario":"J",
            "peso":2},
            {"nodo_primario":"U",
            "nodo_secundario":"Q",
            "peso":6},
            {"nodo_primario":"U",
            "nodo_secundario":"S",
            "peso":11},
            {"nodo_primario":"U",
            "nodo_secundario":"J",
            "peso":5},
            {"nodo_primario":"U",
            "nodo_secundario":"K",
            "peso":13},
            {"nodo_primario":"JJ",
            "nodo_secundario":"A",
            "peso":9},
            {"nodo_primario":"JJ",
            "nodo_secundario":"S",
            "peso":4},
            {"nodo_primario":"A",
            "nodo_secundario":"Y",
            "peso":8},
            {"nodo_primario":"A",
            "nodo_secundario":"JJ",
            "peso":9},
            {"nodo_primario":"A",
            "nodo_secundario":"S",
            "peso":12},
            {"nodo_primario":"A",
            "nodo_secundario":"J",
            "peso":4},
            {"nodo_primario":"S",
            "nodo_secundario":"JJ",
            "peso":4},
            {"nodo_primario":"S",
            "nodo_secundario":"U",
            "peso":11},
            {"nodo_primario":"S",
            "nodo_secundario":"A",
            "peso":12},
            {"nodo_primario":"S",
            "nodo_secundario":"GG",
            "peso":15},
            {"nodo_primario":"I",
            "nodo_secundario":"O",
            "peso":9},
            {"nodo_primario":"I",
            "nodo_secundario":"K",
            "peso":10},
            {"nodo_primario":"K",
            "nodo_secundario":"U",
            "peso":13},
            {"nodo_primario":"K",
            "nodo_secundario":"I",
            "peso":10},
            {"nodo_primario":"O",
            "nodo_secundario":"I",
            "peso":9},
            {"nodo_primario":"O",
            "nodo_secundario":"F",
            "peso":6},
            {"nodo_primario":"O",
            "nodo_secundario":"HH",
            "peso":6},
            {"nodo_primario":"O",
            "nodo_secundario":"L",
            "peso":5},
            {"nodo_primario":"F",
            "nodo_secundario":"O",
            "peso":6},
            {"nodo_primario":"F",
            "nodo_secundario":"OZ",
            "peso":6},
            {"nodo_primario":"F",
            "nodo_secundario":"B",
            "peso":4},
            {"nodo_primario":"OZ",
            "nodo_secundario":"F",
            "peso":6},
            {"nodo_primario":"OZ",
            "nodo_secundario":"J",
            "peso":8},
            {"nodo_primario":"OZ",
            "nodo_secundario":"M",
            "peso":4},
            {"nodo_primario":"HH",
            "nodo_secundario":"O",
            "peso":6},
            {"nodo_primario":"HH",
            "nodo_secundario":"KL",
            "peso":6},
            {"nodo_primario":"P",
            "nodo_secundario":"NN",
            "peso":7},
            {"nodo_primario":"P",
            "nodo_secundario":"G",
            "peso":7},
            {"nodo_primario":"P",
            "nodo_secundario":"V",
            "peso":7},
            {"nodo_primario":"H",
            "nodo_secundario":"Q",
            "peso":9},
            {"nodo_primario":"H",
            "nodo_secundario":"J",
            "peso":6},
            {"nodo_primario":"H",
            "nodo_secundario":"SS",
            "peso":5},
            {"nodo_primario":"J",
            "nodo_secundario":"H",
            "peso":6},
            {"nodo_primario":"J",
            "nodo_secundario":"U",
            "peso":5},
            {"nodo_primario":"J",
            "nodo_secundario":"A",
            "peso":4},
            {"nodo_primario":"J",
            "nodo_secundario":"NN",
            "peso":1},
            {"nodo_primario":"D",
            "nodo_secundario":"NN",
            "peso":6},
            {"nodo_primario":"NN",
            "nodo_secundario":"D",
            "peso":6},
            {"nodo_primario":"NN",
            "nodo_secundario":"S",
            "peso":1},
            {"nodo_primario":"NN",
            "nodo_secundario":"P",
            "peso":1},
            {"nodo_primario":"NN",
            "nodo_secundario":"FF",
            "peso":6},
            {"nodo_primario":"NN",
            "nodo_secundario":"DD",
            "peso":7},
            {"nodo_primario":"NN",
            "nodo_secundario":"YU",
            "peso":6},
            {"nodo_primario":"G",
            "nodo_secundario":"P",
            "peso":7},
            {"nodo_primario":"G",
            "nodo_secundario":"V",
            "peso":19},
            {"nodo_primario":"G",
            "nodo_secundario":"C",
            "peso":5},
            {"nodo_primario":"V",
            "nodo_secundario":"G",
            "peso":19},
            {"nodo_primario":"V",
            "nodo_secundario":"P",
            "peso":7},
            {"nodo_primario":"V",
            "nodo_secundario":"MM",
            "peso":15},
            {"nodo_primario":"SS",
            "nodo_secundario":"H",
            "peso":5},
            {"nodo_primario":"C",
            "nodo_secundario":"GG",
            "peso":5},
            {"nodo_primario":"MM",
            "nodo_secundario":"V",
            "peso":15},
            {"nodo_primario":"DD",
            "nodo_secundario":"NN",
            "peso":7},
            {"nodo_primario":"B",
            "nodo_secundario":"F",
            "peso":4},
            {"nodo_primario":"B",
            "nodo_secundario":"N",
            "peso":7},
            {"nodo_primario":"B",
            "nodo_secundario":"BB",
            "peso":3},
            {"nodo_primario":"BB",
            "nodo_secundario":"B",
            "peso":3},
            {"nodo_primario":"BB",
            "nodo_secundario":"GG",
            "peso":6},
            {"nodo_primario":"N",
            "nodo_secundario":"B",
            "peso":7},
            {"nodo_primario":"N",
            "nodo_secundario":"Z",
            "peso":6},
            {"nodo_primario":"N",
            "nodo_secundario":"CC",
            "peso":6},
            {"nodo_primario":"L",
            "nodo_secundario":"O",
            "peso":5},
            {"nodo_primario":"L",
            "nodo_secundario":"OZ",
            "peso":8},
            {"nodo_primario":"Z",
            "nodo_secundario":"FF",
            "peso":6},
            {"nodo_primario":"Z",
            "nodo_secundario":"N",
            "peso":6},
            {"nodo_primario":"GG",
            "nodo_secundario":"S",
            "peso":15},
            {"nodo_primario":"GG",
            "nodo_secundario":"BB",
            "peso":6},
            {"nodo_primario":"X",
            "nodo_secundario":"CC",
            "peso":6},
            {"nodo_primario":"X",
            "nodo_secundario":"MM",
            "peso":1},
            {"nodo_primario":"CC",
            "nodo_secundario":"M",
            "peso":6},
            {"nodo_primario":"CC",
            "nodo_secundario":"X",
            "peso":6},
            {"nodo_primario":"CC",
            "nodo_secundario":"N",
            "peso":6},
            {"nodo_primario":"M",
            "nodo_secundario":"X",
            "peso":1},
            {"nodo_primario":"M",
            "nodo_secundario":"CC",
            "peso":6},
            {"nodo_primario":"M",
            "nodo_secundario":"OZ",
            "peso":4},
            {"nodo_primario":"FF",
            "nodo_secundario":"Z",
            "peso":6},
            {"nodo_primario":"FF",
            "nodo_secundario":"NN",
            "peso":6},
            {"nodo_primario":"YU",
            "nodo_secundario":"NN",
            "peso":6},
            {"nodo_primario":"YU",
            "nodo_secundario":"FG",
            "peso":6},
            {"nodo_primario":"YU",
            "nodo_secundario":"NM",
            "peso":7},
            {"nodo_primario":"YU",
            "nodo_secundario":"BN",
            "peso":3},
            {"nodo_primario":"YU",
            "nodo_secundario":"LL",
            "peso":8},
            {"nodo_primario":"FG",
            "nodo_secundario":"MM",
            "peso":8},
            {"nodo_primario":"FG",
            "nodo_secundario":"YU",
            "peso":6},
            {"nodo_primario":"FG",
            "nodo_secundario":"RT",
            "peso":5},
            {"nodo_primario":"FG",
            "nodo_secundario":"SD",
            "peso":6},
            {"nodo_primario":"RT",
            "nodo_secundario":"FG",
            "peso":5},
            {"nodo_primario":"RT",
            "nodo_secundario":"SD",
            "peso":5},
            {"nodo_primario":"SD",
            "nodo_secundario":"RT",
            "peso":5},
            {"nodo_primario":"SD",
            "nodo_secundario":"FG",
            "peso":6},
            {"nodo_primario":"SD",
            "nodo_secundario":"QE",
            "peso":7},
            {"nodo_primario":"QE",
            "nodo_secundario":"SD",
            "peso":7},
            {"nodo_primario":"QE",
            "nodo_secundario":"TM",
            "peso":4},
            {"nodo_primario":"QE",
            "nodo_secundario":"LL",
            "peso":5},
            {"nodo_primario":"LL",
            "nodo_secundario":"YU",
            "peso":8},
            {"nodo_primario":"LL",
            "nodo_secundario":"QE",
            "peso":5},
            {"nodo_primario":"IO",
            "nodo_secundario":"PA",
            "peso":5},
            {"nodo_primario":"IO",
            "nodo_secundario":"NM",
            "peso":7},
            {"nodo_primario":"PA",
            "nodo_secundario":"IO",
            "peso":5},
            {"nodo_primario":"PA",
            "nodo_secundario":"KL",
            "peso":8},
            {"nodo_primario":"PA",
            "nodo_secundario":"RC",
            "peso":8},
            {"nodo_primario":"PA",
            "nodo_secundario":"LK",
            "peso":9},
            {"nodo_primario":"NM",
            "nodo_secundario":"YU",
            "peso":7},
            {"nodo_primario":"NM",
            "nodo_secundario":"IO",
            "peso":7},
            {"nodo_primario":"KL",
            "nodo_secundario":"HH",
            "peso":6},
            {"nodo_primario":"KL",
            "nodo_secundario":"PA",
            "peso":8},
            {"nodo_primario":"KL",
            "nodo_secundario":"IU",
            "peso":5},
            {"nodo_primario":"KL",
            "nodo_secundario":"FD",
            "peso":4},
            {"nodo_primario":"HJ",
            "nodo_secundario":"TM",
            "peso":8},
            {"nodo_primario":"TM",
            "nodo_secundario":"HJ",
            "peso":8},
            {"nodo_primario":"TM",
            "nodo_secundario":"BN",
            "peso":2},
            {"nodo_primario":"TM",
            "nodo_secundario":"QE",
            "peso":4},
            {"nodo_primario":"TM",
            "nodo_secundario":"TB",
            "peso":9},
            {"nodo_primario":"TM",
            "nodo_secundario":"TN",
            "peso":8},
            {"nodo_primario":"BN",
            "nodo_secundario":"TM",
            "peso":2},
            {"nodo_primario":"BN",
            "nodo_secundario":"YU",
            "peso":3},
            {"nodo_primario":"BN",
            "nodo_secundario":"CV",
            "peso":1},
            {"nodo_primario":"BN",
            "nodo_secundario":"SD",
            "peso":4},
            {"nodo_primario":"CV",
            "nodo_secundario":"BN",
            "peso":1},
            {"nodo_primario":"CV",
            "nodo_secundario":"UB",
            "peso":2},
            {"nodo_primario":"CV",
            "nodo_secundario":"YT",
            "peso":5},
            {"nodo_primario":"UB",
            "nodo_secundario":"CV",
            "peso":2},
            {"nodo_primario":"TM",
            "nodo_secundario":"QE",
            "peso":4},
            {"nodo_primario":"TN",
            "nodo_secundario":"TM",
            "peso":8},
            {"nodo_primario":"RC",
            "nodo_secundario":"PA",
            "peso":8},
            {"nodo_primario":"EW",
            "nodo_secundario":"TR",
            "peso":7},
            {"nodo_primario":"ON",
            "nodo_secundario":"YT",
            "peso":4},
            {"nodo_primario":"YT",
            "nodo_secundario":"CV",
            "peso":5},
            {"nodo_primario":"YT",
            "nodo_secundario":"ZX",
            "peso":3},
            {"nodo_primario":"YT",
            "nodo_secundario":"TR",
            "peso":5},
            {"nodo_primario":"YT",
            "nodo_secundario":"ON",
            "peso":4},
            {"nodo_primario":"TR",
            "nodo_secundario":"EW",
            "peso":7},
            {"nodo_primario":"TR",
            "nodo_secundario":"ZX",
            "peso":6},
            {"nodo_primario":"TR",
            "nodo_secundario":"YT",
            "peso":5},
            {"nodo_primario":"ZX",
            "nodo_secundario":"TR",
            "peso":6},
            {"nodo_primario":"ZX",
            "nodo_secundario":"YT",
            "peso":3},
            {"nodo_primario":"ZX",
            "nodo_secundario":"SD",
            "peso":2},
            {"nodo_primario":"FD",
            "nodo_secundario":"SA",
            "peso":3},
            {"nodo_primario":"FD",
            "nodo_secundario":"KL",
            "peso":4},
            {"nodo_primario":"FD",
            "nodo_secundario":"LK",
            "peso":3},
            {"nodo_primario":"LK",
            "nodo_secundario":"PA",
            "peso":9},
            {"nodo_primario":"LK",
            "nodo_secundario":"FD",
            "peso":3},
            {"nodo_primario":"JH",
            "nodo_secundario":"OI",
            "peso":2},
            {"nodo_primario":"JH",
            "nodo_secundario":"TB",
            "peso":2},
            {"nodo_primario":"TB",
            "nodo_secundario":"JH",
            "peso":2},
            {"nodo_primario":"TB",
            "nodo_secundario":"TM",
            "peso":9},
            {"nodo_primario":"IU",
            "nodo_secundario":"EC",
            "peso":5},
            {"nodo_primario":"IU",
            "nodo_secundario":"KL",
            "peso":5},
            {"nodo_primario":"IU",
            "nodo_secundario":"OI",
            "peso":5},
            {"nodo_primario":"EC",
            "nodo_secundario":"IU",
            "peso":5},
            {"nodo_primario":"EC",
            "nodo_secundario":"RV",
            "peso":7},
            {"nodo_primario":"OI",
            "nodo_secundario":"IU",
            "peso":5},
            {"nodo_primario":"OI",
            "nodo_secundario":"JH",
            "peso":2},
            {"nodo_primario":"OI",
            "nodo_secundario":"PO",
            "peso":10},
            {"nodo_primario":"RV",
            "nodo_secundario":"FG",
            "peso":4},
            {"nodo_primario":"RV",
            "nodo_secundario":"EC",
            "peso":7},
            {"nodo_primario":"GF",
            "nodo_secundario":"PO",
            "peso":11},
            {"nodo_primario":"GF",
            "nodo_secundario":"SA",
            "peso":12},
            {"nodo_primario":"PO",
            "nodo_secundario":"GF",
            "peso":11},
            {"nodo_primario":"PO",
            "nodo_secundario":"OI",
            "peso":10},
            {"nodo_primario":"PO",
            "nodo_secundario":"SA",
            "peso":4},
            {"nodo_primario":"SA",
            "nodo_secundario":"GF",
            "peso":12},
            {"nodo_primario":"SA",
            "nodo_secundario":"PO",
            "peso":4},
            {"nodo_primario":"SA",
            "nodo_secundario":"FD",
            "peso":3},
        ]

Vertices_small = ["A","B","C","D","E","F"]
Aristas_small = [
            {"nodo_primario":"A",
            "nodo_secundario":"B",
            "peso":7},
            {"nodo_primario":"A",
            "nodo_secundario":"C",
            "peso":9},
            {"nodo_primario":"A",
            "nodo_secundario":"F",
            "peso":14},
            {"nodo_primario":"B",
            "nodo_secundario":"A",
            "peso":7},
            {"nodo_primario":"B",
            "nodo_secundario":"C",
            "peso":10},
            {"nodo_primario":"B",
            "nodo_secundario":"D",
            "peso":15},
            {"nodo_primario":"F",
            "nodo_secundario":"A",
            "peso":14},
            {"nodo_primario":"F",
            "nodo_secundario":"C",
            "peso":2},
            {"nodo_primario":"F",
            "nodo_secundario":"E",
            "peso":9},
            {"nodo_primario":"C",
            "nodo_secundario":"A",
            "peso":9},
            {"nodo_primario":"C",
            "nodo_secundario":"B",
            "peso":10},
            {"nodo_primario":"C",
            "nodo_secundario":"F",
            "peso":2},
            {"nodo_primario":"C",
            "nodo_secundario":"D",
            "peso":11},
            {"nodo_primario":"D",
            "nodo_secundario":"C",
            "peso":11},
            {"nodo_primario":"D",
            "nodo_secundario":"B",
            "peso":15},
            {"nodo_primario":"D",
            "nodo_secundario":"E",
            "peso":6},
            {"nodo_primario":"E",
            "nodo_secundario":"F",
            "peso":9},
            {"nodo_primario":"E",
            "nodo_secundario":"D",
            "peso":9},
            ]