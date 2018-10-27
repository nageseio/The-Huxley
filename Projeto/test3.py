S=[str(i) for i in input().split()]
for i in range(9, -1, -1):
    if 2**i == len(S):
        n=i

def Listbin(n):
    listbin=[]
    for i in range(2**n):
        li=[]
        bini=str('{0:b}'.format(i))
        for x in range(len(bini)):
            li.append(int(bini[x]))
        listbin.append(li)
        while len(listbin[i]) < n:
            listbin[i].insert(0,0)
    return listbin

def Listbin2(a,b,c):
    listbin2=[]
    for i in range(2**b):
        if a[i] == "1":
            listbin2.append(c[i])
    return listbin2

l2 = Listbin2(S,n,Listbin(n))

def Elementos(x):
    list = x
    elementos=[]
    for x in range(n+1):
        l=[]
        for i in list:
            if sum(i) == x:
                l.append(i)
        elementos.append(l)
        while [] in elementos:
            ind = elementos.index([])
            del(elementos[ind])
    return elementos

l3 = Elementos(l2)

def Separador(a):
    elementos = a
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
    return f

l4 = Separador(l3)

li2=[]
li=[]
for i3 in range(n):
    li=[]
    for i2 in l4:
        c = i2.count(1)
        if c == i3:
            li.append(i2)
    li2.append(li)


while [] in li2:
    c = li2.index([])
    del(li2[c])

print(li2)
l44 = Separador(li2)
print(l44)





