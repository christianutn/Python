def fibonacci01(n):
    ant2 = ant1 = 1
    for i in range(2, n+1):
        aux = ant1 + ant2
        ant2 = ant1
        ant1 = aux
    return ant1

n = fibonacci01(5)
print(n)

