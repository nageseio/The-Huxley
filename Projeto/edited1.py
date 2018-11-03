Entrada=[str(i) for i in input().split()] #ENTRADA
for i in range(9, -1, -1):
    if 2**i == len(Entrada):
        Var=i
def Listbin(Var):
    listbin = []
    for i in range(2**Var):
        li = []
        bini = str('{0:b}'.format(i))
        for x in range(len(bini)):
            li.append(int(bini[x]))
        listbin.append(li)
        while len(listbin[i]) < Var:
            listbin[i].insert(0,0)
        listbin[i].insert(0, str(i))
    return listbin

Ma=[]
def Listbin2(a,b,c):
    listbin2=[]

    for i in range(2**b):
        if a[i] == "1":
            listbin2.append(c[i])
    for i in range(len(listbin2)):
        Ma.append(int(listbin2[i][0]))
    return listbin2


l2 = Listbin2(Entrada, Var, Listbin(Var))

def Separador2(a):
    li2 = []
    for i3 in range(Var+1):
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
cc = Separador2(l2)

def Separador(a):
    elementos = a
    f = []
    ff = []
    fr=a
    for i in range(len(elementos)-1):
        for i2 in range(len(elementos[i])):
            for i3 in range(len(elementos[i+1])):
                l = []
                co = 0
                l1 = elementos[i][i2]
                l2 = elementos[i+1][i3]
                li2=[]
                li2.append(l1[0])
                li2.append(l2[0])
                for i4 in range(1,Var+1):
                    if l1[i4] == l2[i4]:
                        l.append(l1[i4])
                    elif l1[i4] != l2[i4]:
                        l.append("-")
                        co += 1
                    if co == Var:
                        ff.append(l1)
                        if (len(elementos)-1) == 1:
                            ff.append(l2)
                if co == 1:
                    l.insert(0,li2)
                    f.append(l)
                    if f != []:
                        fr=f
    if f == []:
        return fr
    else:
        def Separador2(a):
            li2 = []
            for i3 in range(Var + 1):
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
        s=Separador2(f)
        return Separador(s)
ss = (Separador(cc))

F=[]
for i in range(len(ss)):
    for i2 in range(len(ss[i])):
        F.append(ss[i][i2])


for i in F:
    if len(i[0]) > 1:
        while len(i[0])> 1:
            i[0]=(i[0][0]+i[0][1])
            if i[0][1] != list():
                break

#for i in F:
#    if list(i[0]) is True:
#        continue
#    else:
#        i[0]=[i[0]]

c=[]
for i in F:
    c2=[]
    for i2 in range(1,len(i)):
        st= str(i[i2])
        c2.append(st)
    c3=''.join(c2)
    c.append(c3)

Mapa={}
co=0

AB=['A','B','C','D','E','F','G','H','I','J']
for i in AB:
    if co == len(F):
        break
    l=[]
    for i2 in range(len(Ma)):
        l.append(" ")
    Mapa[i]= l
    co+=1

ContadorMapa=0
for i in Mapa:
    for i3 in F[ContadorMapa][0]:
        lu = Ma.index(int(i3))
        Mapa[i][lu]='O'
    if ContadorMapa == len(F):
        break
    else:
        ContadorMapa+=1
print(Mapa)
