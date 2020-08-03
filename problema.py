archivo = open('input.txt')
info = []
for linea in archivo:
    info.append(linea.strip())
archivo.close()

casos = int(info[0])*2
n, p ,s = info[1].split()
cont = 2
lis_casos = []

while cont<=casos:
    matriz = [["" for x in range(len(info[cont+1].split()))] for x in range(len(info[cont].split()))]
    for i in range(len(info[cont].split())):
        for j in range(len(info[cont+1].split())):
            if info[cont].split()[i] == info[cont+1].split()[j]:
                if i == 0 or j == 0:
                    matriz[i][j] = info[cont].split()[i]
                else:
                    matriz[i][j] = matriz[i-1][j-1] + ' ' + info[cont].split()[i]
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1], key=len)
    final= matriz[-1][-1]
    lis_casos.append(final)
    cont+=1


print (lis_casos)