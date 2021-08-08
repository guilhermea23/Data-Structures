qtd = int(input())
habilty = sorted([int(i) for i in input().split()], reverse=True)

if len(habilty) <= 22:
    print(sum(habilty[:11]) - sum(habilty[11:]))
else:
    print(sum(habilty[:11]) - sum(habilty[11:22]))
