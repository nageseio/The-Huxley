lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
v=0
for i in range(1):
  var=int(input())
  if var == 0:
      break
  while True:
    l=int(input())
    if l == 0:
      break
    lista1.append(l)
    lista2.append(int(input()))
    lista3.append(int(input()))
    lista4.append(int(input()))
  def lista(l):
    lista5.append(l)
  for i in range(1):
    lista(lista1)
    lista(lista2)
    lista(lista3)
    lista(lista4)
  for z in range(4):
    lista5[z][z] = lista5[z][z]*var
  for x in range(4):
    for y in range(4):
      print(lista5[x][y],end=" ")
    print()
