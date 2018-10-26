S=[str(i) for i in input().split()]
for i in range(9, -1, -1):
    if 2**i == len(S):
        n=i



listbin=[]
for i in range(2**n):
    listbin.append(str('{0:b}'.format(i)))
    while len(listbin[i])<n:
        listbin[i] = "0"+listbin[i]



listbin2=[]
for i in range(2**n):
    if S[i] == "1":
        listbin2.append(listbin[i])


# SEPARANDO ELEMENTOS
elementos= []
for x in range(n+1):
    l=[]
    for i in listbin2:
        if i.count("1") == x:
            l.append(i)
    elementos.append(l)
    while [] in elementos:
        ind = elementos.index([])
        print(ind)
        del(elementos[ind])


print(elementos[0][0][0])

for i in range(len(elementos)):
    for i2 in range(len(elementos[i][i])):
        for i3 in range(len(elementos[i][i])):
            if elementos[i][i2][i3] == elementos[1][i2][i3]:
                print("ok")



