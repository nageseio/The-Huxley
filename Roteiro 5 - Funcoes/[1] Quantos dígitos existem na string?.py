def Digitos(lista):
  l2=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  qnt=0
  l=0
  for i in range(0,len(lista)):
    if lista[l] in l2:
      qnt+=1
    l+=1
  return qnt
lista=[str(i) for i in input()]
print(Digitos(lista))
