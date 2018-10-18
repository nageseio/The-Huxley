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

    
    lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
so=0
v=0
c=0
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

so+=len(lista1)
so+=len(lista2)
so+=len(lista3)
so+=len(lista4)

cf=0
fc=4
for i in range(int(so/16)):
  def lista(l):
    lista5.append(l)
  for i in range(1):
    lista(lista1[cf:fc])
    lista(lista2[cf:fc])
    lista(lista3[cf:fc])
    lista(lista4[cf:fc])
  for z in range(4):
    lista5[z][z] = lista5[z][z]*var
  for x in range(4):
    for y in range(4):
      print(lista5[x][y],end=" ")
    print()
  print()
  lista5=[]
  cf+=4
  fc+=4
