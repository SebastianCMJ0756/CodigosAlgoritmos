
class Nodito:
    def __init__(self, nombre, lon=None, lat=None, demanda=0, ventana_tiempo=None):
        self.nombre = nombre
        self.lon = lon
        self.lat = lat
        self.vecinos = []
        self.demanda = demanda
        self.ventana_tiempo = ventana_tiempo or (0, 24)

    def __repr__(self):
        return f"Nodito({self.nombre}, lon={self.lon}, lat={self.lat})"

