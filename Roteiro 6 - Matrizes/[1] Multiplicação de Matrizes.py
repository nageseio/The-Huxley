m1,m2,m3,m4,m5,m6,m7=[],[],[],[],[],[],[]
cc,ccc=0,0
var=[int(i) for i in input().split()]
for i in range(var[0]):
  m1.append([int(i) for i in input().split()])
for i in range(var[1]):
  m2.append([int(i) for i in input().split()])
for i in range(var[2]):
  for x in range(var[1]):
    m4.append(m1[cc][x])
  for i in range(var[2]):
    for y in range(var[1]):
      m3.append(m2[y][i])
    for x in range(var[1]): 
      m5.append(m4[x]*m3[x])
    m6.append(sum(m5))
    m5,m3=[],[]
  cc+=1
  ccc=0
  m5,m4,m3=[],[],[]
co,co2,ii=0,var[2],0
for i in range(var[2]):
  m7.append(m6[co:co2])
  for v in range(var[2]-1):
    print(m7[0][ii],end=" ")
    ii+=1
  print(m7[0][ii])
  ii,m7=0,[]
  co+=var[2]
  co2+=var[2]
co,co2=0,var[2]
