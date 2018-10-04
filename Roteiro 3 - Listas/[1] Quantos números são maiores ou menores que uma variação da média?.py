lista=[]
X=0
n1=int(input())
while X<n1:
 lista.append(int(input()))
 X +=1
media = ((sum(lista)/n1))
print("%.2f"%media)
lista2 = []
for i in lista:
    if i*0.9 > media:
        lista2.append(i)
print(len(lista2))
lista3 = []
for i2 in lista:
    if i2*1.1 < media:
        lista3.append(i2)
print(len(lista3))
