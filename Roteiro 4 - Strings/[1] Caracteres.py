x=100000
c=0
i=0
lista=[]
while x > 0:
  n=int(input())
  if n == 0:
    break
  lista = [str(i) for i in input()]
  lista.reverse()
  for v in range(0,n):
    print(lista[i],end="")
    i+=1
  print("")
  i=0
