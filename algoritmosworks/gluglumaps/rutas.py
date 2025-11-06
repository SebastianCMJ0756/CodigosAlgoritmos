import requests
import random

def geocodificar(lugar):
    url = f"https://nominatim.openstreetmap.org/search?q={lugar},Colombia&format=json"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        return (float(r[0]['lon']), float(r[0]['lat'])) if r else None
    except:
        return None

def generar_clientes(num_clientes=10):
    clientes = []
    for i in range(1, num_clientes + 1):
        clientes.append({
            "nombre": f"Cliente_{i}",
            "lon": -74.0 + random.uniform(-0.1, 0.1),
            "lat": 4.6 + random.uniform(-0.1, 0.1),
            "demanda": random.randint(1, 5)
        })
    return clientes

def obtener_distancia(origen, destino):
    url = f"http://router.project-osrm.org/route/v1/driving/{origen[0]},{origen[1]};{destino[0]},{destino[1]}?overview=false"
    r = requests.get(url).json()
    if "routes" in r:
        return r["routes"][0]["distance"] / 1000
    return None

def calcular_distancias(nodos):
    distancias = {}
    for origen in nodos:
        distancias[origen["nombre"]] = {}
        for destino in nodos:
            if origen == destino:
                distancias[origen["nombre"]][destino["nombre"]] = 0
            else:
                d = obtener_distancia(
                    (origen["lon"], origen["lat"]),
                    (destino["lon"], destino["lat"])
                )
                distancias[origen["nombre"]][destino["nombre"]] = d if d else random.uniform(1, 10)
    return distancias
