S=[str(i) for i in input().split()]
for i in range(9, -1, -1):
    if 2**i == len(S):
        n=i


listbin=[]
for i in range(2**n):
    li=[]
    bini=str('{0:b}'.format(i))
    for x in range(len(bini)):
        li.append(int(bini[x]))
    listbin.append(li)
    while len(listbin[i]) < n:
        listbin[i].insert(0,0)

listbin2=[]
for i in range(2**n):
    if S[i] == "1":
        listbin2.append(listbin[i])

# SEPARANDO ELEMENTOS
elementos= []
for x in range(n+1):
    l=[]
    for i in listbin2:
        if sum(i) == x:
            l.append(i)
    elementos.append(l)
    while [] in elementos:
        ind = elementos.index([])
        del(elementos[ind])


f=[]
for i in range(len(elementos)-1):
    for i2 in range(len(elementos[i])):
        for i3 in range(len(elementos[i+1])):
            l=[]
            l1=elementos[i][i2]
            l2=elementos[i+1][i3]
            for i4 in range(n):
                if l1[i4] == l2[i4]:
                    l.append(l1[i4])
                else:
                    l.append("-")
            f.append(l)
print(f)





