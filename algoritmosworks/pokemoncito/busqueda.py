class busqueda:
    def binario(lista, objetivo):
        izquierda, derecha = 0, len(lista) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            if lista[medio] == objetivo:
                return True
            elif lista[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return False