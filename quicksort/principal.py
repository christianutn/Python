def get_pivot(v, izq, der):
    i = (izq + der)//2
    return i

# Para evitar en caer el peor caso, que sería que el valor del pibot sea el menor o el mayor del arreglo
# lo que provocaría que las particiones en vec en vez de ser logaritmicas sean lineales lo cual
# provocaria que el rendimiento total del algoritmo sea exponencial en vec de lineal. Lo que se hace es
# tomar tres elementos del arreglo y el medio de esos tres valores elegirlo como pivot.

def get_pivot_m3(v, izq, der):
    central = (izq + der)//2
    if v[izq] > v[der]:
        v[izq], v[der] = v[der], v[izq]
    if v[central] > v[der]:
        v[central], v[der] = v[der], v[central]
    if v[central] < v[izq]:
        v[central], v[izq] = v[izq], v[central]
    return v[central]

def quick(v, izq, der):
    x = get_pivot(v, izq, der)
    i, j = izq, der
    while i <= j:
        while v[i] < x and i < j:
            i += 1
        while v[j] > x and j > i:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if izq < j:
        quick(v, izq, j)
    if der > i:
        quick(v, i, der)



def quick_sort(v):
    quick(v, 0, len(v)-1)


v = [8, 2, 3, 9, 1, 6, 10]
quick_sort(v)
print(v)
