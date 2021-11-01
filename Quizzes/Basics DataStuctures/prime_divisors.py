def primos_gemeos(n):
    gemeos = []
    p = 3

    def prime(n):
        if n % 2 != 0:
            return True
        return False

    while len(gemeos) < n:
        if prime(p) and prime(p+2):
            gemeos.append((p, p+2))
            p += 2

    print(gemeos[:n])


primos_gemeos(3)
