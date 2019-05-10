def QuantidadeVariaveis(Entrada):
    i=1
    while True:
        if 2**i == len(Entrada):
            return i
        elif 2**i > len(Entrada):
            return 0
        i+=1

def criarListaBinario(Var,ums):
    listbin = []
    listbin2=[]
    for i in range(2**Var):
        li = []
        bini = str('{0:b}'.format(i))
        for x in range(len(bini)):
            li.append(int(bini[x]))
        listbin.append(li)
        while len(listbin[i]) < Var:
            listbin[i].insert(0,0)
        listbin[i].insert(0, [str(i)])
        listbin[i].insert(0, str(' '))
    for i in range(len(ums)):
        if ums[i] == '1':
            listbin2.append(listbin[i])
    return listbin2

def SepararUm1(Lista, Cont, ListaTermos, MAX):
    l=[]
    if Cont > MAX:
        return ListaTermos
    for i in Lista:
        C1 = 0
        for i2 in range(2, len(i)):
            if i[i2] == 1:
                C1+=1;
        if C1 == Cont:
            l.append(i)
    ListaTermos.append(l)
    Cont+=1
    return SepararUm1(Lista, Cont, ListaTermos, MAX)


def Comparar0(L1,L2):
    L=[' ', []]
    M=0
    for i in range(2,len(L1)):
        if L1[i] != L2[i]:
            L.append('-')
            M+=1
        else:
            L.append(L1[i])
    if M == 1:
        L[1] = L1[1]+L2[1]
        return L
    else:
        return []


def Comparar(LB):
    L=[]
    for i in range(len(LB)-1):
        for i2 in LB[i]:
            for i3 in LB[i+1]:
                x = Comparar0(i2,i3)
                if x != []:
                    i2[0] = 'v'
                    i3[0] = 'v'
                    L.append(x)
    for n in range(len(LB)):
        for n2 in LB[n]:
            if n2[0] != 'v':
                L.append(n2)
    return L

def MinimizadorVerificador(Contador, ListaVazia, L):
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, QuantidadeVariaveis)
    Lista2 = Comparar(Lista)
    return Lista2

def Minimizador(Contador, ListaVazia, L):
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, QuantidadeVariaveis)
    Lista2 = Comparar(Lista)
    Contador,ListaVazia = 0,[]
    M = MinimizadorVerificador(Contador, ListaVazia, Lista2)
    if M != Lista2:
        return Minimizador(Contador, ListaVazia, Lista2)
    else:
        return Lista2







def inicializar():
    Entrada = input().split()
    QuantidadeVariaveis = QuantidadeVariaveis(Entrada)
    ListaA = criarListaBinario(QuantidadeVariaveis,Entrada)
    cont,ListaTermos = 0,[]
    ListaB = Minimizador(cont, ListaTermos, ListaA)

inicializar()
