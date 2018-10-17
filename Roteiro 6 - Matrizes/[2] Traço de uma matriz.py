m1=[]
m2=[]
co=0
var=int(input())
for i in range(var):
  m1.append([float(i) for i in input().split()])
for x in range(var):
  m2.append(m1[x][x])
so= sum(m2)
print("tr(A) = ",end="")
for y in range(var-1):
  print("(","%.2f"%(m2[co]),")"," +",sep="",end=" ")
  co+=1
print("(","%.2f"%(m2[co]),")"," = ","%.2f"%so,sep="")
