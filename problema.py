#cantidad de lineas por leer aparte de las primeras 2
casos = int(input().strip())*2
#valores de 'n', 'p' y 's'
n, p ,s = map(int, input().strip().split())

#se almacenan todos los strings en una lista para facilitar su eso
info = list()
for caso in range(casos):
    info.append(input().strip())

#indice para los casos, avanza de 2 en 2
cont = 0

#para guardar los resultados de cada caso
lis_casos = list()

#se itera mientras hayan casos
while cont<casos:
    #matriz para la programación dinámica
    matriz = [["" for x in range(s)] for x in range(p)]

    #secuencia del primer y segundo hijo
    s1 = info[cont].split()
    s2 = info[cont+1].split()

    for i in range(p):
        for j in range(s):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matriz[i][j] = s1[i]
                else:
                    matriz[i][j] = matriz[i-1][j-1] + ' ' + s1[i]
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1], key=len)

    #se añade la posición n,n en la matriz que tiene la respuesta para el string completo
    final= matriz[-1][-1]
    lis_casos.append(final)
    cont+=2

print("\n".join(lis_casos))