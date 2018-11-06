var=[int(x) for x in input().split()]#ENTRADA
lista=['C','K']#MULTIPLICADOR
va=var[0]# QUANTIDADE DE MOEDAS
lt=[]#LISTA ONDE FICAR ARMAZENADA AS PROBABILIDADES
Soma=0#CONATADOR DIFERENCA
D=var[1]# DIFERENCA DESEJADA
def sum(lista,var,lt):
    ck=['C','K']
    if var > 1:
        lt=[]
        for k in range(2):
            l=[]
            for i in range(len(lista)):
                x=ck[k]+lista[i]
                l.insert(0, x)
            for i in range(len(l)):
                lt.append(l[i])
    if len(lt[0]) == var:
        return lt# RETORNO
    return sum(lt,var,lt)# RECURSAO
ll=sum(lista,va,lt)
def Contador(lista2,Soma,D): #lista2 exemplo = [[C,C,C], [C,C,K], [C,K,C], [C,K,K], [K,C,C], [K,C,K], [K,K,C], [K,K,K]]
    for l in lista2:
        ck=l.count('K')
        cc=l.count('C')
        if abs(ck-cc) == D:# DIFERENCA COM MODULO=(abs), caso a diferenca seja negativa
            Soma+=1
    return Soma
print(Contador(ll,Soma,D))
