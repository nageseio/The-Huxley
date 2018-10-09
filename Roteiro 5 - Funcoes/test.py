def sudoku(K):
  l = K
  def sudoku0(l):
    co=0
    for i in range(9):
      lista_s0=[]
      for x in range(9):
        lista_s0.append(l[x][co])
      lista_s1 = ''.join(lista_s0)
      for i in range(1,10):
        s1 = str(lista_s1).count(str(i))
        if s1 == 1:
          r = "s"
          co+=1
        else:
          r = "n"
          break
      
    return r

  def sudoku1(l):
    co=0
    for i in range(9):
      lista_s1= ''.join(l[co])
      for i in range(1,10):
        s1 = str(lista_s1).count(str(i))
        if s1 == 1:
          r = "s"
          co+=1
        else:
          r = "n"
          break
    return r

  def sudoku2(l):
    lista_s=[]
    num1=0
    num2=3
    for i in range(3):
      for x in range(num1,num2):
        for y in range(0,3):
          lista_s.append(l[x][y])
      lista_s1 = ''.join(lista_s)
      for i in range(1,10):
        s1 = str(lista_s1).count(str(i))
        if s1 == 1:
          r = "s"
          lista_s=[]
        else:
          r = "n"
          break
      for x in range(num1,num2):
        for y in range(3,6):
          lista_s.append(l[x][y])
      lista_s1 = ''.join(lista_s)
      for i in range(1,10):
        s1 = str(lista_s1).count(str(i))
        if s1 == 1:
          r = "s"
          lista_s=[]
        else:
          r = "n"
          break
      for x in range(num1,num2):
        for y in range(6,9):
          lista_s.append(l[x][y])
      lista_s1 = ''.join(lista_s)
      for i in range(1,10):
        s1 = str(lista_s1).count(str(i))
        if s1 == 1:
          r = "s"
          lista_s=[]
        else:
          r = "n"
          break
      num1+=3
      num2+=3    
    return r
  if sudoku0(l) == "s" and sudoku1(l) == "s" and sudoku2(l) == "s":
    return "ss"
  else:
    return "nn"
    
lista2=[]
lista3=[]
coo=0
n=int(input())
for x in range(n):
  for i in range(9*n):
    if coo == n:
      break
    lista=[int(i) for i in input().split()]
    lista2.append(lista) 
    print
    nine=0
    nine2=9
  while coo < n:
    lista3 = lista2[nine:nine2]
    if sudoku(lista3) == "ss":
      print("\nInstancia ",x+1,"\nSIM",sep="")
      x+=1
    if sudoku(lista3) == "nn":
      print("\nInstancia ",x+1,"\nNAO",sep="")
      x+=1
    if coo == n:
      break
    lista3=[]
    nine+=9
    nine2+=9
    coo+=1
    
    
    
    
    lista_s0=['8', '7', '9', '6', '4', '2', '1', '3', '5']
lista_s1= ''.join(lista_s0)
for i in range(1,10):
  print(str(lista_s1).count(str(i)))
