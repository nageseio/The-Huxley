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
print(Ma)

ff=[]
fr=[]
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
    print(ff,"ff")
    if f == []:
        if fr == []:
            if ff == []:
                return exc
            return ff
        return fr
    else:
        return SeparadorTermos(f,ff,fr)

print(ff)
print(SeparadorTermos(l2,ff,fr),"l2")
