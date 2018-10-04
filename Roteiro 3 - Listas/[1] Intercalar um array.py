lista=[]
lista2=[]
lista3=[]
X=0
X2=0
X3=0
X4=0
li=0
li2=0
li3=0
n1=int(input())
while X < n1:
  lista.append(int(input()))
  X +=1
while X2 < n1:
  lista2.append(int(input()))
  X2 +=1
elementos = len(lista)+len(lista2)
while li < n1:
  if X3 < n1+1:
    lista3.append(lista[li])
    li+=1
    X3+=1
  if X4 < n1+1:
    lista3.append(lista2[li2])
    li2+=1
    X4+=1
for i in range(0, elementos):
 print(lista3[li3])
 li3+=1
