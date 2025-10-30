#       Torre Hanoi
#////       ////     ////     ////     

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def imprimir_matriz(torres, max_discos):
    matriz = []
    for _ in range(max_discos):
        fila = [" ", " ", " "]  
        matriz.append(fila)

    nombres = ["A", "B", "C"]
    for columna in range(3):
        torre_columna = torres[nombres[columna]]  
        for pos in range(len(torre_columna)):
            fila_idx = max_discos - len(torre_columna) + pos
            matriz[fila_idx][columna] = torre_columna[pos]

    for fila in matriz:
        print(fila)
    print("-" * 25)  


def torre_hanoi(n, origen, destino, auxiliar, torres, contador, max_discos):
    if n == 1:

        if not torres[origen]:
            raise ValueError(f"Torre {origen} está vacía al intentar mover un disco.")
        disco = torres[origen].pop()
        torres[destino].append(disco)
        contador[0] += 1

        print(f"Paso {contador[0]}: mover disco {disco} de {origen} a {destino}")
        imprimir_matriz(torres, max_discos)
        indice = busqueda_lineal(torres[destino], disco)
        print(" -> Índice del disco buscado (lineal):", indice)
        return


    torre_hanoi(n - 1, origen, auxiliar, destino, torres, contador, max_discos)


    if not torres[origen]:
        raise ValueError(f"Torre {origen} está vacía al intentar mover un disco.")
    disco = torres[origen].pop()
    torres[destino].append(disco)
    contador[0] += 1
    print(f"Paso {contador[0]}: mover disco {disco} de {origen} a {destino}")
    imprimir_matriz(torres, max_discos)
    indice = busqueda_lineal(torres[destino], disco)
    print(" -> Índice del disco buscado (lineal):", indice)


    torre_hanoi(n - 1, auxiliar, destino, origen, torres, contador, max_discos)


if __name__ == "__main__":
    n = 3
    torres = {
        "A": [3, 2, 1],  
        "B": [],
        "C": []
    }

    print("Estado inicial:")
    imprimir_matriz(torres, n)

    torres["A"] = bubble_sort(torres["A"])

    contador = [0]

    torre_hanoi(n, "A", "C", "B", torres, contador, n)