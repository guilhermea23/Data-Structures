def fibonacci(n):
    fib = []
    a = 0
    b = 1
    if n == 0:
        return fib
    if n == 1:
        fib.append(a)
    else:
        fib.append(b-1)
        fib.append(b)

        for i in range(2, n):
            c = a+b
            fib.append(c)
            a = b
            b = c
    return fib


n = int(input())
print(fibonacci(n))
