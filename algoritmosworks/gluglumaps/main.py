from grafo import Grafo
from rutas import generar_clientes, calcular_distancias

def main():
    print("Optimización de rutas de entrega (versión simplificada) ")

    
    grafo = Grafo()

    
    grafo.agregar("Almacén", lon=-74.05, lat=4.65, demanda=0)

    clientes = generar_clientes(num_clientes=10)
    for c in clientes:
        grafo.agregar(c["nombre"], lon=c["lon"], lat=c["lat"], demanda=c["demanda"])

    
    distancias = calcular_distancias([{"nombre": "Almacén", "lon": -74.05, "lat": 4.65}] + clientes)
    for o in distancias:
        for d in distancias[o]:
            grafo.conectar(o, d, distancias[o][d])

    
    grafo.mostrar()

    
    capacidad = 20
    rutas = grafo.asignar_vehiculos(capacidad)

    print("\nAsignación de vehículos:")
    for i, ruta in enumerate(rutas):
        print(f"Vehículo {i+1}: Almacén → {' → '.join(ruta)} → Almacén")

if __name__ == "__main__":
    main()
