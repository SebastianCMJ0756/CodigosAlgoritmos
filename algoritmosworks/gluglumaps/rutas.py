
import requests

def geocodificar(lugar):

    url = f"https://nominatim.openstreetmap.org/search?q={lugar},Colombia&format=json"
    respuesta = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
    return (respuesta[0]['lon'], respuesta[0]['lat']) if respuesta else None


def ruta_calculo(origen, parada, destino):

    puntos = [geocodificar(origen)]
    if parada:
        puntos.append(geocodificar(parada))
    puntos.append(geocodificar(destino))

    if None in puntos:
        return None

    coordenadas = ";".join([f"{lon},{lat}" for lon, lat in puntos])
    url = f"http://router.project-osrm.org/route/v1/driving/{coordenadas}?overview=false&steps=true"
    respuesta = requests.get(url).json()

    if "routes" not in respuesta:
        return None

    rutas = respuesta["routes"][0]["legs"]


    def sumar_distancias(indice=0):
        return 0 if indice == len(rutas) else rutas[indice]["distance"] + sumar_distancias(indice + 1)

    def sumar_tiempos(indice=0):
        return 0 if indice == len(rutas) else rutas[indice]["duration"] + sumar_tiempos(indice + 1)

    distancia_km = sumar_distancias() / 1000
    tiempo_segundos = sumar_tiempos()
    return distancia_km, tiempo_segundos
