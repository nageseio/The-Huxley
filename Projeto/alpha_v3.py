S=[str(i) for i in input().split()] #ENTRADA
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
    ff=[]
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
                        elif elementos[i][i4] == elementos[i3][i4]:
                            l.append(elementos[i][i4])
                    if '-' in l and c == 1:
                        f.append(l)
                    elif '-' in l and c == n:
                        ff.append(elementos[i])
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
    ff=[]
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
                    elif l1[i4] != l2[i4]:
                        l.append("-")
                        co+=1
                    if co == n:
                        ff.append(l1)
                if co == 1:
                    f.append(l)
    return ff
ss=(Separador2(l2))
cc=(Separador(ss))
ss1=(Identififcador(l2))
ss2=(Identififcador(ss1))
def SimpCC(x):
    cc=x
    ccc=cc[:]
    if len(cc) > 1:
        for i in range(len(cc)-1):
            for i2 in range(n):
                if cc[i][i2] == cc[i+1][i2]:
                    ccc[i][i2]=('-')
                    ccc[i+1][i2]=('-')
                print()
        return ccc
    else:
        return cc
xc=SimpCC(cc)
if cc != [] and ss2 != []:
    for i in range(len(xc)):
        ss2.append(xc[i])
    ss3=ss2[:]
    for i in ss3:
        co=ss2.count(i)
        if co > 1:
            co2=ss2.index(i)
            del(ss2[co2])
    FF=ss2
elif cc == [] and ss2 != []:
    FF=ss2
elif cc == [] and ss2 == []:
    FF=l2
def Org(a):
    Alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
CA=Org(FF)
def Org2(CA):
    x=0
    lf=[]
    for i in range(len(CA)):
        for i2 in range(len(CA[i])):
            lf.append(CA[i][i2])
        if len(CA) > 1 and x != len(CA)-1:
            lf.append("+")
            x+=1
    return ''.join(lf)
QUINE=Org2(CA)
def Org3():
    TT0=["A'","B'","C'","D'","E'","F'","G'","H'","I'","J'","K'","L'","M'","N'","O'","P'","Q'","R'","S'","T'","U'","V'","W'","X'","Y'","Z'",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in TT0:
        if QUINE.count(i) == len(FF) and ss2 != [] and len(CA)>1:
            return i
    return QUINE
QUINE2=Org3()#SAIDA = QUINE2
print(QUINE2)
