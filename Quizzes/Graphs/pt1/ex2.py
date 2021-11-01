class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.arestas = dict()

    def insertVertice(self, vertice):
        self.graphNodos.append(vertice)

    def removeVertice(self, vertice):
        self.graphNodos.pop(self.graphNodos.index(vertice))

    def insertAresta(self, origem, destino):
        if origem and destino:
            self.arestas[origem] = destino

    def removeAresta(self, origem, destino):
        del self.arestas[origem]


n = int(input())
graph = Graph()
for i in range(n):
    instruction = input().split()
    if instruction[0] == 'IV':
        graph.insertVertice(instruction[1])
    elif instruction[0] == 'IA':
        graph.insertAresta(instruction[1], instruction[2])
    elif instruction[0] == 'RV':
        pass
    else:
        pass
