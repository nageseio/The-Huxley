l=0
l2=0
l3=0
l4=0
lista=[]
lista2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '-']
S=1
while 0 < S: 
  n=input().upper()
  if n == "FIM":
    break
  for i in range(len(n)):
    lista.append(n[l])
    l+=1
  l=0
  if "O" in lista:
    for i in range(len(lista)):
      if lista[l2] == "O":
        lista[l2] = "0"
      l2+=1
    l2=0
  if "L" in lista:
    for i in range(len(lista)):
      if lista[l2] == "L":
        lista[l2] = "1"
      l2+=1
    l2=0
  n2 = ''.join(lista)
  for i in range(len(lista2)):
    if lista2[l3] in n2:
      l4+=1
    l3+=1
  l3=0
  if l4 >0:
    print("ERRO")
  elif l4 == 0:
    print(int(n2))
  l4=0
  lista=[]
