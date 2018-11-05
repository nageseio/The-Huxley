var=[int(x) for x in input().split()]
co=0
def Listbin(n,co):
    listbin = []
    for i in range(2**n):
        li = []
        bini = str('{0:b}'.format(i))
        for x in range(len(bini)):
            li.append(int(bini[x]))
        listbin.append(li)
        while len(listbin[i]) < n:
            listbin[i].insert(0,0)
    if 2**n == co:
        return listbin
    co+=1
    return Listbin(n,co)

bini=Listbin(var[0],co)
bini2=bini[:]
for i in bini:
    qntc=i.count(0)
    qntk=i.count(1)
    if abs(qntc-qntk) != var[1]:
        ind=bini2.index(i)
        del(bini2[ind])
for i in bini:
    for i2 in range(len(i)):
        if i[i2] == 0:
            i[i2]='C'
        else:
            i[i2]='K'
x=(len(bini2))
print(x)
f=0
i=0
def Diferenca(lista,f,i,x):
    if x == i:
        return f
    k=lista[i].count('K')
    c=lista[i].count('C')
    if abs(c-k) == var[1]:
        f+=1
    i+=1
    return Diferenca(lista,f,i,x)
#print(Diferenca(bini,f,i,x))
