class PokeGrafo:
    def __init__(self):
        self.grafo = {}     #Se guarda toda la info de las evoluciones

    def gradobuild(self, chain):
        Nombre= chain['species']['name']        #Pokemon actual
        #Lista de evoluciones
        self.grafo[Nombre] = [evol['species']['name'] for evol in chain.get('evolves_to', [])]

        for evolucion in chain.get('evolves_to', []):
            self.gradobuild(evolucion)
    
    def getgrafo(self, data):
        self.gradobuild(data['chain'])
        return self.grafo