lista=[]
lista2=[]
X=0
i=0
n1=int(input())
while X < n1:
  lista.append(int(input()))
  X +=1
n2=int(input())
lista2 = lista[0:n2]
del(lista[0:n2])
lista3 = lista+lista2
for i in range(0,len(lista3)):
 print(lista3[i])
 i+=1
