casos = int(input().strip())*2
n, p ,s = map(int, input().strip().split())
info = list()
for caso in range(casos):
    info.append(input().strip())


cont = 0
lis_casos = list()

while cont<casos:
    matriz = [["" for x in range(s)] for x in range(p)]
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
    final= matriz[-1][-1]
    lis_casos.append(final)
    cont+=2


print("\n".join(lis_casos))