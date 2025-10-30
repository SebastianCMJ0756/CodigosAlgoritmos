
def busqueda_binaria(lista, valor, inicio=0, fin=None):

    fin = len(lista) - 1 if fin is None else fin

    if inicio > fin:
        return False

    medio = (inicio + fin) // 2

    if lista[medio] == valor:
        return True
    elif lista[medio] < valor:
        return busqueda_binaria(lista, valor, medio + 1, fin)
    else:
        return busqueda_binaria(lista, valor, inicio, medio - 1)
