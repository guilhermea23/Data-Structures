class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def addAresta(self, u, v, tg, peso):
        # grafo direcionado simples
        if tg == 'D':
            # trocar o igual por += se for grafo múltiplo
            self.grafo[u-1][v-1] = peso
        else:
            # trocar o igual por += se for grafo múltiplo
            self.grafo[u-1][v-1] = peso
            self.grafo[v-1][u-1] = peso

        # self.grafo[v-1][u-1] se o grafo for não direcionado

    def mostraMatriz(self):
        for i in range(self.vertices):
            for j in self.grafo[i]:
                print(f'{j}   ',end='')
            print()


vertices, arestas, tg = input().split()
vertices,arestas = int(vertices),int(arestas)
g = Grafo(vertices)
for n in range(arestas):
    origem, destino, peso = [int(x) for x in input().split()]
    g.addAresta(origem, destino, tg, peso)

g.mostraMatriz()
