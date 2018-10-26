S=[str(i) for i in input().split()]
for i in range(9, -1, -1):
    if 2**i == len(S):
        n=i
listbin=[]
for i in range(2**n):
    listbin.append(str('{0:b}'.format(i)))
    while len(listbin[i])<n:
        listbin[i] = "0"+listbin[i]
listbin2=[]
for i in range(2**n):
    if S[i] == "1":
        listbin2.append(listbin[i])


elementos= {}
for x in range(n+1):
    for i in listbin2:
        if i.count("1") == x:
            elementos[x] = elementos.get(x, i)
print(elementos)
