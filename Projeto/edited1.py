


d={}
d[1]='A'
print(d)
d[2]='B','C'
s = str(d[1])
s2 = str(d[2][0])
print(s+s2)

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


c=[]
for i in F:
    c2=[]
    for i2 in range(1,len(i)):
        st= str(i[i2])
        c2.append(st)
    c3=''.join(c2)
    c.append(c3)
print(c)

d={}
co=0
for i in Ma:
    l=[]
    for i2 in range(len(F)):
        l.append(" ")
    d[i]= l,c[co]
    co+=1

print(F)
print(d)
print(Ma,"ma")
for i in d:
  for i3 in i2[0]:
      i3=Ma.index(int(i3))
      d[i][0][i3]='O'
  print(d,"d")
