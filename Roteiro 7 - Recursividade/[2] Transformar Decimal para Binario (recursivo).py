n0=int(input())
l=[]
def Binario(n0):
    if n0 == 1:
        return 1
    elif n0 == 0:
        return 0
    r = n0%2
    l.append(r)
    t = n0//2
    if t == 1:
        l.append(n0//2)
        for i in range(1,len(l)+1):
            print(l[-i])
        quit()
    return Binario(t)
print(Binario(n0))
