n = int(input())
iras = []
for i in range(n):
    ira = float(input())
    iras.append(ira)
iras.sort()

while iras != []:
    x = iras.pop()
    print(f'{x:.2f}')
