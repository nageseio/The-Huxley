fd=[[' ', ['0', '2'], 0, 0, 0, '-', 0], [' ', ['2', '10'], 0, '-', 0, 1, 0], [' ', ['9', '25'], '-', 1, 0, 0, 1], [' ', ['10', '26'], '-', 1, 0, 1, 0], [' ', ['20', '22'], 1, 0, 1, '-', 0], [' ', ['15', '31'], '-', 1, 1, 1, 1], [' ', ['0', '1', '4', '5'], 0, 0, '-', 0, '-'], [' ', ['1', '5', '9', '13'], 0, '-', '-', 0, 1], [' ', ['4', '5', '12', '13'], 0, '-', 1, 0, '-'], [' ', ['4', '5', '20', '21'], '-', 0, 1, 0, '-'], [' ', ['4', '12', '20', '28'], '-', '-', 1, 0, 0], [' ', ['9', '11', '13', '15'], 0, 1, '-', '-', 1], [' ', ['10', '11', '14', '15'], 0, 1, '-', 1, '-'], [' ', ['12', '13', '14', '15'], 0, 1, 1, '-', '-']]
cx2=[['-', 0, 1, 0, '-'], [1, 0, 1, '-', 0], ['-', 1, 0, 0, 1], ['-', 1, 0, 1, 0], ['-', '-', 1, 0, 0], ['-', 1, 1, 1, 1]]
Var=5
Ma=[0, 1, 2, 4, 5, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 25, 26, 28, 31]
fx=fd[:]
AB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z']

def FMapa(cxx):
    Mapa,co={},0
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

Mapa3=FMapa(fx)
Mapaind=[]

for i in Mapa3:
    Mapaind.append(Mapa3[i])
mm2 = Mapaind[:]
lista = []
Mapa2 = []
if mm2 != {}:
    listae=[]
    lco=[]
    for i in Mapa3:
        Mapa2.append(i)
    for x in range(1):
        Elementos = []
        for y in range(len(Mapaind)):
            Elementos.append(Mapaind[y][x])
    for x in range(len(Mapaind[0])):
        c = []
        for y in range(len(Mapaind)):
            c.append(Mapaind[y][x])
        if c.count('O') == 1:
            lco.append(x)
            ind = c.index('O')
            listae.append(Elementos[ind])
    for x in range(len(Mapaind[0])):
        for y in range(len(Mapaind)):
            if x in lco:
                if type(Mapaind[y][x]) != list:
                    Mapaind[y][x]=' '
Mapa={}
co=0
for i in AB:
    if len(Mapa) == len(Mapaind):
        break
    Mapa[i]= Mapaind[co]
    co+=1
Mapa2=Mapaind[:]

Mapaind=[]
for i in AB:
    if len(Mapa2) == len(Mapaind):
        break
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
print(Ma)
print("Mapa2",Mapa2,'Mapa2','Mapa',Mapa,"Mapa")
lista = OnPatrick(Mapa2, f)

while [] in lista:
    ind=lista.index([])
    del(lista[ind])


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
            b=i+i2
            l.append(b)
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
print(len(xx))
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
print(c)
Mapaf={}
for i in Mapa:
    Mapaf[i]=Mapa[i]
l=[]
for i in Mapaf:
    for i2 in c:
        if i2 == i:
            l.append(Mapaf[i][0])

print(l)
print(ultimafuncao(l),'6')
