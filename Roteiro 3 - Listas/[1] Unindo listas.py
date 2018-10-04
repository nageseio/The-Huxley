lista=[]
X=0
n=-1
n2=0
n3=0
X2=0
while X < 2:
  n1=int(input())
  if n1 == 0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
    break
  n3 = n3+n1
  X +=1
  for i in range(0,n1):
    lista.append(int(input()))
  n1=0
if X == 2:
  for i in range(0,n3-1):
    print(lista[n2],end=" ")
    n2+=1
  print(lista[n2])
