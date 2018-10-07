def listas(lista):
  lista=[]
  l=0
  for i in range(0, 3):
    lista.append(n[l])
    l+=1
  lista.sort()
  return lista
n=[int(i) for i in input().split()]
print(listas(n)[2])
