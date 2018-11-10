Entrada=[str(i) for i in input().split()] #ENTRADA
i=0
while True:
    if 2**i == len(Entrada):
        Var=i
        break
    i+=1
def ListaBinario(Var):
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
        listbin[i].insert(0, str(' '))
    return listbin
Ma=[]
def ListaImplicantes(a,b,c):
    listbin2=[]
    for i in range(2**b):
        if a[i] == "1":
            listbin2.append(c[i])
    for i in range(len(listbin2)):
        Ma.append(int(listbin2[i][1]))
    return listbin2

l2 = ListaImplicantes(Entrada, Var, ListaBinario(Var))

ff,fr=[],[]
def SeparadorTermos(a,ff,fr):
    f=a
    fr=f
    lista = []
    for i3 in range(Var+1):
        li = []
        for i2 in a:
            quantidadede1s = i2.count(1)
            if quantidadede1s == i3:
                li.append(i2)
        lista.append(li)
    while [] in lista:
        quantidadede1s = lista.index([])
        del (lista[quantidadede1s])
    f = []
    for i in range(len(lista)-1):
        for i2 in range(len(lista[i])):
            for i3 in range(len(lista[i+1])):
                l = []
                li2=[]
                co = 0
                l1,l2 = lista[i][i2],lista[i+1][i3]
                li2.append(l1[1])
                li2.append(l2[1])
                for i4 in range(2,Var+2):
                    if l1[i4] == l2[i4]:
                        l.append(l1[i4])
                    elif l1[i4] != l2[i4]:
                        l.append("-")
                        co += 1
                if co != 1:
                    if lista[i][i2][0] == 'v' and lista[i+1][i3][0] != 'v':
                        ff.append(l2)
                    elif lista[i][i2][0] != 'v' and lista[i+1][i3][0] == 'v':
                        ff.append(l1)
                    elif lista[i][i2][0] != 'v' and lista[i+1][i3][0] != 'v':
                        ff.append(l1)
                        ff.append(l2)
                if co == 1:
                    if lista[i][i2] in ff:
                        ind = ff.index(lista[i][i2])
                        del(ff[ind])
                    if lista[i + 1][i3] in ff:
                        ind = ff.index(lista[i + 1][i3])
                        del(ff[ind])
                    lista[i][i2][0]='v'
                    lista[i + 1][i3][0]='v'
                    l.insert(0,li2)
                    l.insert(0, ' ')
                    f.append(l)
                if f != []:
                    fr=f
                    exc=ff
    if f == []:
        if fr == []:
            if ff == []:
                return exc
            return ff
        return fr+ff
    else:
        return SeparadorTermos(f,ff,fr)
dc=SeparadorTermos(l2,ff,fr)
for i in dc:
    if type(i[1]) != list:
        i[1]=[i[1]]
for i in dc:
    if type(i[1][0]) == list:
        for i2 in range(len(i[1])-1):
            l=i[1][i2]+i[1][i2+1]
        i[1]=l
dx=dc[:]
for i in range(len(dc)):
    for i2 in range(len(dc)):
        if i != i2:
            c=0
            l1=[]
            l2=[]
            for i3 in range(2,Var+2):
                l1.append(dc[i][i3])
            for i4 in range(2, Var + 2):
                l2.append(dc[i2][i4])
            if l1 == l2:
                if dc[i2][0] == 'v' or dc[i2][0]=='v':
                    break
                else:
                    if dc[i2] in dx:
                        ind=dx.index(dc[i2])
                        del(dx[ind])
                        dc[i2][0]= 'v'
                        dc[i][0]= 'v'
for i in dx:
    i[0]=' '
dc,co=dx[:],0
def Eraser(lista,co):
    c=lista.count(lista[co])
    if c>1:
        del(lista[co])
    else:
        co+=1
    if c ==1:
        cx=0
        for i in lista:
            cx+=lista.count(i)
        if cx == len(lista):
            return lista
    return Eraser(lista,co)
cxx=Eraser(dc,co)
Mapa,co={},0
AB=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in AB:
    if co == len(cxx):
        break
    l=[]
    for i2 in range(len(Ma)):
        l.append(" ")
    Mapa[i]= l
    co+=1
ContadorMapa=0
for i in Mapa:
    for i3 in cxx[ContadorMapa][1]:
        lu = Ma.index(int(i3))
        Mapa[i][lu]='O'
        l2=[]
    for n2 in range(2,Var+2):
      l2.append(cxx[ContadorMapa][n2])
    Mapa[i].insert(0, l2)
    if ContadorMapa == len(cxx):
        break
    else:
        ContadorMapa+=1
Mapa2=[]
for i in Mapa:
    Mapa2.append(Mapa[i])
Contador = 0
def Patrick(Mapa,Contador):
    for x in range(len(Mapa2[0])):
        c=[]
        for y in range(len(Mapa2)):
            c.append(Mapa2[y][x])
        if c.count('O') > 1:
            Contador+=1
    if Contador == len(Ma):
        return 'OnPatrick'
    else:
        return 'NoPatrick'
P=Patrick(Mapa2,Contador)
Contador,list=0,[]
def Organizer(Mapa,Contador,list):
    for x in range(len(Mapa2[0])):
        c=[]
        for y in range(len(Mapa2)):
            c.append(Mapa2[y][x])
        if c.count('O') == 1:
            ind=c.index('O')
            list.append(Mapa[ind][0])
    for i in list:
        if list.count(i) > 1:
            ind = list.index(i)
            list[ind]= []
    while [] in list:
        ind = list.index([])
        del(list[ind])
    return list
cx2=(Organizer(Mapa2,Contador,list))
def Essenciais(Mapa,c):
    for i in c:
        for x in Mapa:
            if i != x[0]:
                c= c+[x[0]]
                return c
if P == 'NoPatrick':
    if len(cx2) == 2 and len(Mapa2) > 2:
        print(Essenciais(Mapa2,cx2))
    else:
        print(cx2)
else:

    Mapaind = []
    for i in Mapa:
        Mapaind.append(i)
    f = []

    def OnPatrick(Mapa2, f):
        for x in range(len(Mapa2[0])):
            c = []
            l = []
            for y in range(len(Mapa2)):
                c.append(Mapa2[y][x])
                if Mapa2[y][x] == 'O':
                    ind = c.index('O')
                    l.append(Mapaind[ind])
                    c[ind] = '0'
            f.append(l)
        del (f[0])
        return f
    list = OnPatrick(Mapa2, f)
    def Rec(list, l):
        if len(list) == 1:
            l.append(list[0])
            list = l[:]
            l = []
        if len(list) > 1 or list == []:
            if list != []:
                f = []
                l2 = list[1]
            else:
                f = []
                list = l[:]
                l = []
                l2 = list[1]
            for i in list[0]:
                for i2 in l2:
                    f.append(i + i2)
            l.append(f)
        if len(l) == 1 and len(list) == 2:
            return f
        if len(list) > 1:
            if len(list) == 2:
                list = []
            else:
                del (list[0])
                if len(list) > 1:
                    del (list[0])
        return Rec(list, l)
    l = []
    list2, co, c = Rec(list, l), 0, 'ABCDEFGHIJ'
    for i in list2:
        l = []
        for i2 in range(len(i)):
            l.append(i[i2])
        for i3 in l:
            if l.count(i3) > 1:
                ind = l.index(i3)
                del (l[ind])
        list2[co] = ''.join(l)
        co += 1
    print(list2)
    for i in list2:
        if len(i) <= len(c):
            c = i
    print(Mapa)
    print(c)
