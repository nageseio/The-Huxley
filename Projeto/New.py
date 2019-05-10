def QuantidadeVariaveis(Entrada):#Determina a quantida de variaveis a partir da Entrada.
    i=1
    while True:
        if 2**i == len(Entrada):
            return i
        elif 2**i > len(Entrada):
            return 0
        i+=1

def criarListaBinario(Var,ums):#Cria a lista em binaro com base na quantidade de variaveis e descartas os termos irrevelantes.
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

def SepararUm1(Lista, Cont, ListaTermos, MAX):#Sepera os termos em listas diferentes, pela quantidade de 1's em cada termo.
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


def Comparar0(L1,L2):#Compara dois termos e verifica se a comparação e o termo obitido será valido
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


def Comparar(LB):#Seleciona os termos que serao comparados, e retorna uma lista contendo as comparaçoes.
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

def MinimizadorVerificador(Contador, ListaVazia, L):#função secundaria de Minimizador, para determinar uma parada valida
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, QuantidadeVariaveis)
    Lista2 = Comparar(Lista)
    return Lista2

def Minimizador(Contador, ListaVazia, L):#Usa as funcoes criadas para manipular os termos e retornar elementos validos, que serao usados para formar o mapa dos implicantes(termos).
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, QuantidadeVariaveis)
    Lista2 = Comparar(Lista)
    Contador,ListaVazia = 0,[]
    M = MinimizadorVerificador(Contador, ListaVazia, Lista2)
    if M != Lista2:
        return Minimizador(Contador, ListaVazia, Lista2)
    else:
        return Lista2

def Diferenciador(I0,I1):#Verificar se dois termos são iguais.
    if I0 != [] and I1 != []:
        if I0[2::] == I1[2::]:
            return True
        else:
            return False
    return False

def LimparRepetidos(Lista):#Verifica se existe elementos repetidos e os remove.
    for i in range(len(Lista)):
        for i2 in range(len(Lista)):
            if i != i2:
                if Diferenciador(Lista[i],Lista[i2]) == True:
                    Lista[i2]= []
    while [] in Lista:
        del(Lista[Lista.index([])])
    return Lista


def criarMapa(Lista,QV):#Cria o mapa, que possibilita a extração dos implicantes, para obter a expresão minimizada
    Mapa={}
    l=[]
    l2=[]
    for i in Lista:
        for i2 in i[1]:
            if int(i2) not in l2:
                l2.append(int(i2))
    l2.sort()
    for i2 in range(len(l2)):
        l.append(' ')
    for i in range(len(Lista)):
        Mapa[str(i)] = [Lista[i][1]]+[l[:]]
    for i in Mapa:
        for i2 in Mapa[i][0]:
            Mapa[i][1][l2.index(int(i2))] = 'O'
    return Mapa

def verificadorPetrick(mapa):
    Maux=[]
    for i in mapa:
        Maux.append(mapa[i][1])
    contador1 = 0
    for x in range(len(Maux[0])):
        contador2 = 0
        for y in range(len(Maux)):
            if Maux[y][x] == 'O':
                contador2+=1
        if contador2 > 1:
            contador1+=1
    if contador1 == len(Maux[0]):
        return True
    else:
        return False

def Final(mapa):
    l2=[]
    for x in range(len(mapa['0'][1])):
        l = []
        for i in mapa:
                if mapa[i][1][x] == 'O':
                    l.append(i)
        l2.append(l)
    return l2


def Multiplicador(Termo1,Termo2):
    M=[]
    for i in Termo1:
        for i2 in Termo2:
            if i2== i:
                M.append(i)
            elif i2 not in i:
                x = i+i2
                if x not in M:
                    M.append(x)
    return M



def Extracao(Lista):
    ListaExt=[]
    x = len(Lista)
    if x == 1:
        return Lista
    if x%2 == 0:
        c1=0
        c=1
        for i in range(int(x/2)):
            y = Multiplicador(Lista[c1],Lista[c])
            ListaExt.append(y)
            c1+=2
            c+=2
    else:
        c1=0
        c=1
        for i in range((x//2)):
            ListaExt.append(Multiplicador(Lista[c1],Lista[c]))
            c1+=2
            c+=2
        ListaExt.append(Lista[-1])
    return Extracao(ListaExt)





Entrada = input().split()
QuantidadeVariaveis = QuantidadeVariaveis(Entrada)
ListaA = criarListaBinario(QuantidadeVariaveis,Entrada)
cont,ListaTermos = 0,[]
ListaB = Minimizador(cont, ListaTermos, ListaA)
ListaC = LimparRepetidos(ListaB)

Mapa = criarMapa(ListaC,QuantidadeVariaveis)
print(Mapa)
x = verificadorPetrick(Mapa)

x2 = Final(Mapa)

x3 = Extracao(x2)


def ExtracaoPetrick(Lista,mapa):
    c=9999
    ii=''
    for i in x3[0]:
        c2=0
        for i2 in Mapa:
            if i2 in i:
                c2+=1
        if c2 < c:
            c = c2
            ii=i
    return ii

def Substituicao(Termo,mapa):
    l=[]
    l2=[]
    for i in Termo:
        if i not in l:
            l.append(i)
    for i in l:
        l2.append(mapa[i][0])
    return l2


x4 = ExtracaoPetrick(x3,Mapa)

x5 = Substituicao(x4,Mapa)
print(ListaC)
print(x5)
