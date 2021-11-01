def soma(nList):
    i = 0
    while len(nList) != 1:
        print(f'{nList[i]} + soma({nList[1:]})')
        nList.pop(0)
        if len(nList) == 1:
            break
    print(nList[0])


n = int(input())

numbers = []
for i in range(1, n+1):
    numbers.append((2*i-1))

soma(numbers)
print('---------------')
print(f'{n} ** 2 == {n**2}')
