var=int(input())
def CA(x,y):
  A=x
  D=y
  Q=x//y
  R=x%y
  if R == 0:
    return D
  elif A == D*Q+R and R > 0:
    y=R
    x=D
    return CA(x,y)
for i in range(var):
  List=[int(i) for i in input().split()]
  print("MDC(",List[0],",",List[1],") = ",CA(List[0],List[1]),sep="")
