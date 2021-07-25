
def Sieve_Eratosthenes(n):
  primes = []
  for i in range(2,1000):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            primes.append(i)
            j = j + 1
        else:
            j = j + 1
  return primes
qtd = int(input()) # Qtd tuples in list.
print(Sieve_Eratosthenes(qtd)) # Call a function to return prime numbers
