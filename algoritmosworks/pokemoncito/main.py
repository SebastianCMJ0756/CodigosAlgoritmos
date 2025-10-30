from apipoke import APIPOKE
from grafipoke import PokeGrafo
from busqueda import busqueda

def main():
    url= "https://pokeapi.co/api/v2/evolution-chain/1/"
    #   Obtiene los datos de la API
    API= APIPOKE(url)
    Data= API.ObtencionDatos()

    grafo= PokeGrafo()
    grafipoke= grafo.getgrafo(Data)
    print("Grafo de evoluciones obtenido:   ")
    #   Resultados de las evoluciones
    for pokemon, evoluciones in grafipoke.items():
        print(f"{pokemon} -> {evoluciones}")
    # Listica ordenada de pokemones
    PokeOrdenados= sorted(grafipoke.keys())
    print("\nPokémon ordenados alfabéticamente:")
    print(PokeOrdenados)

if __name__ == "__main__":
    main()
