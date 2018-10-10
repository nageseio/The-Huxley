def insta0(lista):
  v1,v2,v3=0,1,2
  for i in range(9):
    for x in range(1,2):
      if str(x) in l4[v1]+l4[v2]+l4[v3]:
        resp0 = "s"
        print("aqui 1")
      else:
        resp0 = "n"
        print("aqui 1")
        break
    v1+=3
    v2+=3
    v3+=3
  return resp0
def insta1(lista):
  v1,v2,v3=0,3,6
  for i in range(3):
    for x in range(1,2):
      if str(x) in l4[v1]+l4[v2]+l4[v3]:
        resp = "s"
        print("aqui 2")
      else:
        resp = "n"
        print("aqui 2")
        break
    v1+=1
    v2+=1
    v3+=1
  v1,v2,v3=9,12,15
  for i in range(3):
    for x in range(1,2):
      if str(x) in l4[v1]+l4[v2]+l4[v3]:
        resp = "s"
        print("aqui 3")
      else:
        resp = "n"
        print("aqui 3")
        break
    v1+=1
    v2+=1
    v3+=1
  v1,v2,v3=18,21,24
  for i in range(3):
    for x in range(1,2):
      if str(x) in l4[v1]+l4[v2]+l4[v3]:
        resp = "s"
        print("aqui 4")
      else:
        resp = "n"
        print("aqui 4")
        break
    v1+=1
    v2+=1
    v3+=1
  return resp
def insta2(lista):
  v1,v2,v3=0,1,2
  l5=[]
  for i in range(9):
    l5.append(lista[v1]+lista[v2]+lista[v3])
    v1+=3
    v2+=3
    v3+=3
  co=0
  for i in range(9):
    lista_s0=[]
    for x in range(9):
      lista_s0.append(l5[x][co])
    for i in range(1,10):
      if str(i) in lista_s0:
        resp2 = "s"
        print("aqui 5")
      else:
        resp2 = "n"
        print("aqui 5")
        break
    co+=1
  return resp2
n=int(input())
nine=0
nine2=9
g=0
for i in range(n):
  li2=[]
  for i in range(9):
    lista=[str(i) for i in input().split()]
    li2.append(lista)
  li2 = li2[nine:nine2]
  v1=0
  v2=3
  l4=[]
  for i in range(9):
    for x in range(3):
      l4.append(li2[i][v1:v2])
      v1+=3
      v2+=3
    v1=0
    v2=3
  nine+=0
  nine2+=9
  if insta0(l4) == "s" and insta1(l4) == "s" and insta2(l4) == "s":
    print("\nInstancia ",g+1,"\nSIM",sep="")
    g+=1
  else:
    print("\nInstancia ",g+1,"\nNAO",sep="")
    g+=1
