def JOGO(var):
  C=0
  if var[0]+1 == var[1] and var[1]+1 == var[2]:
    C += var[0]
  if var[0] == var[1] and var[0] == var[2]:
    C += var[0]
  var.sort()
  if var[0] == var[1] and var[2] > var[1]:
    C += var[1]/2
  if var[1] == var[2] and var[0] < var[2]:
    C += var[0]/2
  if sum(var) == 8:
    C += 8
  print(C,"c")
  return C
num1=[int(i) for i in input().split()]
num2=[int(i) for i in input().split()]
if JOGO(num1) == JOGO(num2):
  print(0)
elif JOGO(num1) > JOGO(num2):
  print(1)
elif JOGO(num1) < JOGO(num2):
  print(2)
