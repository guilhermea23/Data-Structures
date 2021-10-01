from math import ceil
n = int(input())

consumos = []

for i in range(n):
    qtd, cons = map(int, input().split())
    consumoMedio = cons/qtd
    ceil(consumoMedio)
    consumos.append((consumoMedio, qtd))

consumos.sort()
i = 0
while consumos != []:
    x = consumos.pop()
    index = consumos.index(x)
    if x[0] in consumos:
        consumos.insert(i+1, x)
    print(x[0], x[1], sep=" / ")
    i += 1
