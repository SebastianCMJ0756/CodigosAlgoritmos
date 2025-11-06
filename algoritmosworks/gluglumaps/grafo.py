
from nodo import Nodito

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.distancias = {}  # la matriz de las distancias entre los  nodos

    def agregar(self, nombre, lon=None, lat=None, demanda=0, ventana_tiempo=None):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodito(nombre, lon, lat, demanda, ventana_tiempo)

    def conectar(self, origen, destino, distancia):
        if origen not in self.distancias:
            self.distancias[origen] = {}
        self.distancias[origen][destino] = distancia

    def mostrar(self):
        print("\nUbicaciones registradas:")
        for nombre, nodo in self.nodos.items():
            print(f"{nombre} (Demanda: {nodo.demanda}, Ventana: {nodo.ventana_tiempo})")

    def asignar_vehiculos(self, capacidad_vehiculo):
        clientes = [n for n in self.nodos.values() if n.nombre != "Almacén"]
        rutas = []
        vehiculo = []
        carga_actual = 0
        for c in clientes:
            if carga_actual + c.demanda <= capacidad_vehiculo:
                vehiculo.append(c.nombre)
                carga_actual += c.demanda
            else:
                rutas.append(vehiculo)
                vehiculo = [c.nombre]
                carga_actual = c.demanda
        if vehiculo:
            rutas.append(vehiculo)
        return rutas
