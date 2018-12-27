la = [str(i) for i in input()]
lb = [str(i) for i in input()]
def Lista(lista):
    if len(lista)%2 == 1:
        va2 = len(lista)//2
        va1 = va2+1
    else:
        va2 = int(len(lista) / 2)
        va1 = va2
    nla1=[]
    nla2=[]
    for i in range(va1):
        nla1.append(lista[i])
    for i in range(1,va2+1):
        nla2.append(lista[-i])
    nla1.sort()
    nla2.sort()
    return nla1,nla2
LA = Lista(la)
LB = Lista(lb)
F=0
if LA[0] == LB[0] and LA[1] == LB[1]:
    F+=1
elif LA[0] == LB[1] and LA[1] == LB[0]:
    F+=1
if F != 0:
    print('YES')
else:
    print('NO')
