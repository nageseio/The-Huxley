lista=[]
X=0
n2=0
n=int(input())
if n == 0:
  print("Numero de notas invalido.")
else:
  while X < n:
    lista.append(float(input()))
    X +=1
  media = (sum(lista)/n)
  for i in range(0, n):
    print("Nota ",n2+1,": ",lista[n2],sep="")
    n2+=1
  print("Media:","%.2f"%media)
