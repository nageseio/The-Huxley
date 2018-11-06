def Titio(a,b,c,d):
    if a[c]%2 == 0:
        d+=a[c]*2*b
        b-=1
    elif a[c]%2 == 1:
        d+=a[c]*3*b
        b-=1
    if b == 0:
        return print(d)
    c+=1
    return Titio(a,b,c,d)
l=[]
while True:
    n=str(input())
    if n == '0':
        break
    l.append(n)
for i in l:
    c = 0
    f = 0
    q = len(i)
    l2=[]
    for i2 in range(len(i)):
        l2.append(int(i[i2]))
    Titio(l2,q,c,f)
