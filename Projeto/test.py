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
elementos= {}
for x in range(n+1):
    l=[]
    for i in listbin2:
        if i.count("1") == x:
            l.append(i)
    elementos[x] = l
    if elementos[x] == []:
        del(elementos[x])


print(elementos)
print(elementos[2][0][0],"\n",len(elementos[2]),"\n",elementos[2],"\n")


for e in elementos:
    for x in range(len(elementos[e])):
        for y in range(n):
            for z in range(len(elementos[e+1])):
