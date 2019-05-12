def quantidadeVariaveis(Entrada):#Determina a quantida de variaveis a partir da Entrada.
    n=1
    while True:
        if 2**n == len(Entrada):
            return n
        elif 2**n > len(Entrada):
            return 0
        n+=1

def criarListaBinario(Var,ums):#Cria a lista em binaro com base na quantidade de variaveis e descartas os termos irrevelantes.
    listabin = []
    listabin2=[]
    for i in range(2**Var):
        li = []
        bin = str('{0:b}'.format(i))
        for x in range(len(bin)):
            li.append(int(bin[x]))
        listabin.append(li)
        while len(listabin[i]) < Var:
            listabin[i].insert(0,0)
        listabin[i].insert(0, [str(i)])
        listabin[i].insert(0, str(' '))
    for i in range(len(ums)):
        if ums[i] == '1':
            listabin2.append(listabin[i])
    return listabin2

def SepararUm1(Lista, Cont, ListaTermos, MAX):#Sepera os termos em listas diferentes, pela quantidade de 1's em cada termo.
    l=[]
    if Cont > MAX:
        return ListaTermos
    for i in Lista:
        C1 = 0
        for i2 in range(2, len(i)):
            if i[i2] == 1:
                C1+=1
        if C1 == Cont:
            l.append(i)
    ListaTermos.append(l)
    Cont+=1
    return SepararUm1(Lista, Cont, ListaTermos, MAX)

def Comparar0(termo1,termo2):#Compara dois termos e verifica se a comparação e o termo obitido será valido
    L=[' ', []]
    M=0
    for i in range(2,len(termo1)):
        if termo1[i] != termo2[i]:
            L.append('-')
            M+=1
        else:
            L.append(termo1[i])
    if M == 1:
        L[1] = termo1[1]+termo2[1]
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

def MinimizadorVerificador(Contador, ListaVazia, L, qntvar):#função secundaria de Minimizador, para determinar uma parada valida
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, qntvar)
    Lista2 = Comparar(Lista)
    return Lista2

def Minimizador(Contador, ListaVazia, L, qntvar):#Usa as funcoes criadas para manipular os termos e retornar elementos validos, que serao usados para formar o mapa dos implicantes(termos).
    Contador,ListaVazia = 0,[]
    Lista = SepararUm1(L, Contador, ListaVazia, qntvar)
    Lista2 = Comparar(Lista)
    Contador,ListaVazia = 0,[]
    M = MinimizadorVerificador(Contador, ListaVazia, Lista2, qntvar)
    if M != Lista2:
        return Minimizador(Contador, ListaVazia, Lista2, qntvar)
    else:
        return Lista2

def Diferenciador(termo0,termo1):#Verificar se dois termos são iguais.
    if termo0 != [] and termo1 != []:
        if termo0[2::] == termo1[2::]:
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

def verificadorPetrick(mapa):#Verifica quando usar o Metodo Petrick
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

def essentialPrimeImplicants(mapa):#Encontra os termos essenciais,implicantes primos
    l2=[]
    for x in range(len(mapa['0'][1])):
        l = []
        for i in mapa:
                if mapa[i][1][x] == 'O':
                    l.append(i)
        l2.append(l)
    return l2

def Multiplicador(Termo1,Termo2):#Multiplica variaveis em listas, retorna resultadoda multiplicação
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

def ExtracaoPetrick(Lista):#Retorna um lista contendo as possibilidas, da expressao minimizada
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
    return ExtracaoPetrick(ListaExt)

def EncontrarExpressao(Lista,mapa):#Verifica qual o termo mais minimizado
    c=9999
    ii=''
    for i in Lista[0]:
        c2=0
        for i2 in mapa:
            if i2 in i:
                c2+=1
        if c2 < c:
            c = c2
            ii=i
    return ii

def VerificarTermosMapa(Termos,mapa):#Verifica o mapa, a partir do termo reduzido e retorna seu represetente
    listatermos,listatermosessenciais=[],[]
    for variavel in Termos:
        if variavel not in listatermos:
            listatermos.append(variavel)
    for termo in listatermos:
        listatermosessenciais.append(mapa[termo][0])
    return listatermosessenciais

def SubstituirVaririaveis(listadeimplicantes,termosessenciais):#Faz a substituicao dos binarios por variaveis
    listavariaveissub=[]
    for i in range(len(listadeimplicantes)):
        for i2 in range(len(termosessenciais)):
            if termosessenciais[i2] == listadeimplicantes[i][1]:
                bins = listadeimplicantes[i][2::]
                listavariaveis=[]
                for i3 in range(len(bins)):
                    letra = chr(ord('A') + i3)
                    if bins[i3] == 1:
                        listavariaveis.append(letra)
                    elif bins[i3] == 0:
                        listavariaveis.append(letra+"'")
                listavariaveissub+=[listavariaveis]
    return listavariaveissub

def OrganizarVariaveis(variaveis):#Organiza as variaveis, adicionas as expressoes de soma e multiplicação, se necessario
    l=[]
    c=0
    for i in range(len(variaveis)):
        if c != i:
            l.append('+')
        c2=0
        for i2 in range(len(variaveis[i])):
            if c2 != i2:
                l.append('.')
            l.append(variaveis[i][i2])
    return "".join(l)

def Comecar(Entrada):
    QuantidadeVariaveis = quantidadeVariaveis(Entrada)
    ListaA = criarListaBinario(QuantidadeVariaveis,Entrada)
    contador,ListaTermos = 0,[]
    ListaB = Minimizador(contador, ListaTermos, ListaA, QuantidadeVariaveis)
    ListaC = LimparRepetidos(ListaB)
    Mapa = criarMapa(ListaC,QuantidadeVariaveis)
    PrimosEssenciais = essentialPrimeImplicants(Mapa)
    combinacoesPetrick = ExtracaoPetrick(PrimosEssenciais)
    TermoReduzido = EncontrarExpressao(combinacoesPetrick,Mapa)
    TermosEssenciais = VerificarTermosMapa(TermoReduzido,Mapa)
    Variaveis = SubstituirVaririaveis(ListaC,TermosEssenciais)
    TermoMinimizado = OrganizarVariaveis(Variaveis)
    print(TermoMinimizado)

Comecar(input().split())
