Entrada=[str(i) for i in input().split()]
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
def ultimafuncao(n):
    ultimalista=''
    string=''
    barrado=["A'","B'","C'","D'","E'","F'","G'","H'","I'","J'","K'","L'","M'","N'","O'","P'","Q'","R'","S'","T'","U'","V'","W'","X'","Y'","Z'"]
    normal=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in n:
        for x in range(len(i)):
            if i[x]!='-':
                if i[x]==0:
                    ind=i.index(0)
                    i[x]=barrado[ind]
                elif i[x]==1:
                    ind=i.index(1)
                    i[x]=normal[ind]
            else:
                i[x]=''
    cont1=0
    for i in n:
        li=''.join(i)
        if li not in ultimalista:
            ultimalista+=li
        cont2=(len(n)-1)
        if len(n)>1:
            if cont1!=cont2:
                cont1+=1
                if ultimalista[-1] != '+':
                    ultimalista+='+'
    if ultimalista[-1] == '+':
        l=[]
        for i in range(len(ultimalista)):
            l.append(ultimalista[i])
        del(l[-1])
        l=''.join(l)
        ultimalista=l
    uiop = ultimalista
    return(uiop)
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
                for i4 in range(2,len(l1)):
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
for i in dx:
    if i[0] == 'v':
        ind=dx.index(i)
        dx[ind]=[]
while [] in dx:
    ind=dx.index([])
    del(dx[ind])
def DC(list):
    dc=list
    x=len(dc)
    for i in range(len(dc)):
        l1 = dc[i]
        for i2 in range(len(dc)):
            if i != i2:
                c=0
                l2=dc[i2]
                if l1 == []:
                    break
                if l2 == []:
                    break
                for i3 in range(2,len(l1)):
                    if l1[i3] == l2[i3]:
                        c+=1
                if c == Var:
                    ind=dc.index(l2)
                    dc[ind]=[]
    while [] in dc:
        ind=dc.index([])
        del(dc[ind])
    if x == len(dc):
        return dc
    return DC(dc)
fd=DC(dx)
for i in fd:
    co=fd.count(i)
    if co > 1:
        ind=fd.index(i)
        fd[ind]=[]
while [] in fd:
    ind=fd.index([])
    del(fd[ind])
cxx=fd
l=[]
for i in cxx:
  if len(i[1]) > 1 and type(i[1][0]) == list:
    for i2 in range(len(i[1])):
      l=l+i[1][i2]
    i[1]=l
    l=[]
def FMapa(cxx):
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
    return Mapa
Mapa=FMapa(cxx)
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
    if len(Entrada) == len(Ma):
        print(1,'1')
    elif len(cx2) == 2 and len(Mapa2) > 2:
        cx2=(Essenciais(Mapa2,cx2))
        print(ultimafuncao(cx2),'2')
    elif len(cx2) == 1 and len(cxx[0][1]) == len(Ma):
      print(ultimafuncao(cx2),'3')
    else:
        cx3=cx2[:]
        def Who(list, list2):
            list3 = list2[:]
            for i in list:
                l = []
                co = 0
                if i != []:
                    for i2 in range(2, len(i)):
                        l.append(i[i2])
                for i3 in list2:
                    if l == i3:
                        ind = list3.index(i3)
                        list3[ind].insert(0, i[1])
                        ind = list.index(i)
                        list[ind] = []
            while [] in list:
                ind = list.index([])
                del (list[ind])
            for i in list:
                if i != []:
                    for i2 in list3:
                        if i != []:
                            for i3 in i[1]:
                                if i3 in i2[0]:
                                    if i in list:
                                        ind = list.index(i)
                                        list[ind] = []
                                        break
            while [] in list:
                ind = list.index([])
                del (list[ind])
            return list
        ele = Who(fd, cx2)
        Mapa = FMapa(ele)
        Mapa2 = []
        for i in Mapa:
            Mapa2.append(Mapa[i])
        def Who2(ele, fd):
            list = fd
            list2 = list[:]
            for i in list:
                co = 0
                for i2 in i[1]:
                    if i2 in ele:
                        co += 1
                if co > 0:
                    ind = list.index(i)
                    list2[ind] = []
            while [] in list2:
                ind = list2.index([])
                del (list2[ind])
            return list2


        mm2 = Mapa
        lista = []
        Mapa2 = []
        if Mapa == {}:
            for i in cx3:
                ll = []
                if type(i[0]) == type(ll):
                    del (i[0])
            print(ultimafuncao(cx3),'7')
        else:
            for i in mm2:
                Mapa2.append(mm2[i])
            for x in range(len(Mapa2[0])):
                c = []
                for y in range(len(Mapa2)):
                    c.append(Mapa2[y][x])
                if c.count('O') == 1:
                    ind = c.index('O')
                    lista.append(Mapa2[ind][0])
            for i in cx2:
                ll=[]
                if type(i[0]) == type(ll):
                    del (i[0])
            print(fd)
            for i in fd:
                ll=[]
                if i[0]!= type(ll):
                    del(i[0])
                if type(i[0]) == type(ll):
                    del (i[0])
            cx2 = (lista + cx2)
            if len(fd) == 1:
                cx2=cx2+fd
            print(cx2)
            print(ultimafuncao(cx2),'211')
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
    lista = OnPatrick(Mapa2, f)
    f = []
    def Rec(list, f):
        if list == []:
            list = f[:]
            f = []
        if len(list) == 1:
            f.append(list[0])
            list = f[:]
            f = []
        l = []
        for i in list[0]:
            for i2 in list[1]:
                l.append(i + i2)
        f.append(l)
        if len(f) == 1 and len(list) == 2:
            return l
        if len(list) == 2:
            del (list[0])
            del (list[0])
        if len(list) > 1:
            del (list[0])
            if len(list) != 1:
                del (list[0])
        return Rec(list, f)
    xx = Rec(lista, f)
    list2,co,c,cv = xx,0,'',0
    for i in list2:
        l = []
        for i2 in range(len(i)):
            l.append(i[i2])
        for i3 in l:
            if l.count(i3) > 1:
                ind = l.index(i3)
                l[ind] = '0'
        co += 1
        xc = ''.join(l)
        ind = list2.index(i)
        list2[ind] = xc
    for i in list2:
        if i.count('0') >= cv:
            x = i.count('0')
            cv = x
            c = i
    Mapaf={}
    for i in Mapa:
        Mapaf[i]=Mapa[i]
    l=[]
    for i in Mapaf:
        for i2 in c:
            if i2 == i:
                l.append(Mapaf[i][0])
    print(ultimafuncao(l),'6')
