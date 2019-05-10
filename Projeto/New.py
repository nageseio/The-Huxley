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







Entrada = input().split()
QuantidadeVariaveis = QuantidadeVariaveis(Entrada)
ListaA = criarListaBinario(QuantidadeVariaveis,Entrada)
cont,ListaTermos = 0,[]
ListaB = Minimizador(cont, ListaTermos, ListaA)
ListaC = LimparRepetidos(ListaB)

for i in ListaC:
    print(i)


