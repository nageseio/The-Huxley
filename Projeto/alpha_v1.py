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
def Identififcador(a):
    elementos = a
    f=[]
    if len(elementos) > 1:
        for i in range(len(elementos)):
                for i3 in range(len(elementos)):
                    l=[]
                    c=0
                    for i4 in range(n):
                        #print(i,i4," ",i3,i4)
                        if elementos[i][i4] != elementos[i3][i4]:
                            l.append('-')
                            c+=1
                        else:
                            l.append(elementos[i][i4])
                    if '-' in l and c == 1:
                        f.append(l)
        f2=f[:]
        for i in f:
            if f2.count(i) != 1:
                valor = f2.index(i)
                del(f2[valor])
        return f2
    else:
        return elementos
def Separador2(a):
    li2 = []
    for i3 in range(n):
        li = []
        for i2 in a:
            c = i2.count(1)
            if c == i3:
                li.append(i2)
        li2.append(li)
    while [] in li2:
        c = li2.index([])
        del (li2[c])
    return li2
def Separador(a):
    elementos = a
    f=[]
    for i in range(len(elementos)-1):
        for i2 in range(len(elementos[i])):
            for i3 in range(len(elementos[i+1])):
                l=[]
                co=0
                l1=elementos[i][i2]
                l2=elementos[i+1][i3]
                for i4 in range(n):
                    if l1[i4] == l2[i4]:
                        l.append(l1[i4])
                    else:
                        l.append("-")
                        co+=1
                if co == 1:
                    f.append(l)
    f2=f[:]
    for i in f:
        if f2.count(i) != 1:
            valor = f2.index(i)
            del(f2[valor])
    return f2
def Mini(a):
    l2=[]
    for i in range(len(a)-1):
        l=[]
        for i2 in range(n):
            if a[i][i2] != a[i+1][i2]:
                l.append('-')
            else:
                l.append(a[i][i2])
        l2.append(l)
    l3=l2[:]
    for i in l3:
        c = l3.count(i)
        if c != 1:
            v = l2.index(i)
            del(l2[v])
    return l2
sss=Identififcador(l2)
i2=Identififcador(sss)
if i2 != []:
    F = Identififcador(sss)
elif sss != []:
    F = sss
else:
    F = l2
def Org(a):
    Alpha=['A','B','C','D']
    lll=[]
    for i in range(len(a)):
        l=[]
        for i2 in range(n):
            if a[i][i2] == '-':
                continue
            elif a[i][i2] == 0:
                l.append(Alpha[i2]+"'")
            elif a[i][i2] == 1:
                l.append(Alpha[i2])
        lll.append(l)
    return lll
CA=Org(F)
def Cu(CA):
    x=0
    for i in range(len(CA)):
        for i2 in range(len(CA[i])):
            print(CA[i][i2],end="")
        if len(CA) > 1 and x != len(CA)-1:
            print("+",end="")
            x+=1
Cu(CA)
