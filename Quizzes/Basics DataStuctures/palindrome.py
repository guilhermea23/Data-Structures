empthy = input().lower()
inverse = empthy[::-1]

dif = 0
for i in range(len(empthy)):
    if empthy[i] != empthy[-(i+1)]:
        dif += 1
dif = int(dif/2)
if dif == 1:
    print('POSSÍVEL')
elif empthy == inverse and len(empthy) % 2 == 0:
    print('IMPOSSÍVEL')
else:
    print('IMPOSSÍVEL')
