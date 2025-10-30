
from nodo import Nodito

class Grafo:

    def __init__(self):
        self.nodos = {}

    def agregar(self, origen, destino):

        if origen not in self.nodos:
            self.nodos[origen] = Nodito(origen)
        if destino not in self.nodos:
            self.nodos[destino] = Nodito(destino)
        self.nodos[origen].vecinos.append(destino)

    def mostrar(self):

        print("\nUbicaciones y conexiones:")
        for nombre, nodo in self.nodos.items():
            print(f"{nombre} → {nodo.vecinos}")
