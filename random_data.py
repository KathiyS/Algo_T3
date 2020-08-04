from random import randint, sample
#from numpy import uni

casos = 10
n = 4
p = 6
s = 8

print(f"{casos}\n{n} {p} {s}")

muestra = range(2, n*n)

for i in range(casos):
    print(1, end=" ")
    print(" ".join(map(str, sorted(sample(muestra, p-2)))), end=" ")
    print(n*n)

    print(1, end=" ")
    print(" ".join(map(str, sorted(sample(muestra, s-2)))), end=" ")
    print(n*n)