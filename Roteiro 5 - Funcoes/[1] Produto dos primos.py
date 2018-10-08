def Primo(lista):
  l=0
  primo=0
  for i in range(0,len(lista)):
    n = lista[l]
    i = 1
    j = 0
    n2 = (n/2)
    while (i <= n):
      if (n % i==0):
          i = i+1
          j = j+1
      if (i>=n2):
          i = n
          i = i+1
          j = j+1
      else:
          i = i+1
    if(j==2):
      primo+=1
    if n < 2:
      return "SEM PRODUTO"
      break
    l+=1
  if len(lista) == primo:
    return lista[0]*lista[1]*lista[2]*lista[3]
  elif len(lista) != primo:
    return "SEM PRODUTO"
lista=[int(i) for i in input().split()]
print(Primo(lista))
