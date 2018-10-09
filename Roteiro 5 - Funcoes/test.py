def sudoku(K):
  l = K
  def sudoku0(l):
    co=0
    for i in range(9):
      lista_s0=[]
      for x in range(9):
        lista_s0.append(l[x][co])
      ci=''.join(lista_s0)
      for i in range(1,10):
        s1 = str(ci).count(str(i))
        if s1 == 1:
          r = "s"
        else:
          r = "n"
          break
      co+=1
    return r

  def sudoku1(l):
    co=0
    for i in range(9):
      ci=''.join(l[co])
      for i in range(1,10):
        s1 = str(ci).count(str(i))
        if s1 == 1:
          r = "s"
        else:
          r = "n"
          break
      co+=1
    return r

  def sudoku2(l):
    ci2=['1','2','3']
    ci4=[]
    ci6=[]
    lista_s=[]
    num1=0
    num2=3
    for i in range(3):
      for x in range(num1,num2):
        for y in range(0,3):
          lista_s.append(str(l[x][y]))
        ci2 = ci2+lista_s
        ci = ''.join(ci2[3:12])
        print(ci)
        for i in range(1,10):
          s1 = str(ci).count(str(i))
          if s1 == 1:
            r = "s"
          else:
            r = "n"
            break
          lista_s=[]
      for x in range(num1,num2):
        for y in range(3,6):
          lista_s.append(str(l[x][y]))
        ci4 = ci4+lista_s
        ci3 = ''.join(ci4[3:12])
        print(ci3)
        for i in range(1,10):
          s1 = str(ci3).count(str(i))
          if s1 == 1:
            r = "s"
          else:
            r = "n"
            break
          lista_s=[]
      for x in range(num1,num2):
        for y in range(6,9):
          lista_s.append(l[x][y])
        ci6 = ci6+lista_s
        ci5 = ''.join(ci6[9:18])
        print(ci5)
        for i in range(1,10):
          s1 = str(ci6).count(str(i))
          if s1 == 1:
            r = "s"
          else:
            r = "n"
            break
      num1+=3
      num2+=3 
      ci2=[]
      ci4=[]
      ci6=[]
      lista_s=[]   
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
    lista=[str(i) for i in input().split()]
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
