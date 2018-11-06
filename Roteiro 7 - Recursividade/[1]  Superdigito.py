D=[str(x) for x in input().split()]
D=D[0]*int(D[1])
def Superdigito(li):
    lis=[]
    for i in range(len(li)):
        lis.append(int(li[i]))
    l=str(sum(lis))
    if len(l) == 1:
        return l
    return Superdigito(l)
print(Superdigito(D))
