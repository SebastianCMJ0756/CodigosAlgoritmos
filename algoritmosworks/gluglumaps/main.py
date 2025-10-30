# main.py
from grafo import Grafo
from rutas import ruta_calculo
from busquedita import busqueda_binaria

def main():
    print("""   ____Calculeo de rutas en colombia____
          _____________________________________________           
          """)

    origen = input("Ingrese el Origen: ")
    parada = input("Ingrese la Parada: ")
    destino = input("Ingrese el Destino: ")

    resultado = ruta_calculo(origen, parada, destino)

    if resultado:
        distancia_total, tiempo_total = resultado
        horas = int(tiempo_total // 3600)
        minutos = int((tiempo_total % 3600) // 60)

        grafo_ruta = Grafo()
        grafo_ruta.agregar(origen, parada if parada else destino)
        grafo_ruta.agregar(parada if parada else origen, destino)
        grafo_ruta.mostrar()

        lugares = sorted([l for l in [origen, parada, destino] if l])
        encontrado = busqueda_binaria(lugares, origen)

        print(f"Ruta: {', '.join(lugares)}")
        print(f"Distancia total: {distancia_total:.2f} km")
        print(f"Tiempo estimado de viaje: {horas} h y {minutos} min")
        print(f"¿El origen está en la lista? {'Sí' if encontrado else 'No'}")
    else:
        print("No fue posible calcular la ruta. Verifique los nombres ingresados.")

if __name__ == "__main__":
    main()
