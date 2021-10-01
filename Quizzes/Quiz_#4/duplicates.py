n = int(input())
clothes = [x for x in input().split()]

l = []
equals = 0
for cloth in clothes:
    if cloth not in l:
        l.append(cloth)
    else:
        equals += 1
print(equals)
