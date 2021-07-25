qtd = int(input())
i=0
for i in range(qtd):
  s = input()
  count = 0
  for j in range(len(s)-1):
    if s[j] == '1' and s[j+1]==0:
      count = count + 1
  print(count)