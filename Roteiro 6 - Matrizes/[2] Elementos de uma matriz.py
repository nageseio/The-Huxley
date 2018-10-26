li=[]
li2=[]
ma0=0
me0=0
ma=[int(i) for i in input().split()]
for i in range(ma[0]):
  for i2 in range(ma[1]):
    li.append(int(input()))
  li2.append(li)
  li=[]
print("Matriz formada:")
for x in range(ma[0]):
  for y in range(ma[1]-1):
    print(li2[x][y],end=" ")
  print(li2[x][y+1])
if ma[0]==ma[1]:
  dp=0
  ds=0
  for v in range(ma[0]):
    dp+=li2[v][v]
  v3=1
  for v2 in range(ma[0]):
    ds+=li2[v2][-v3]
    v3+=1
  print("A diagonal principal e secundaria tem valor(es)",dp,"e",ds,"respectivamente.")
else:
  print("A diagonal principal e secundaria nao pode ser obtida.")
for x in range(ma[0]):
  for y in range(ma[1]):
    if li2[x][y] > 0:
      ma0+=1
    elif li2[x][y] < 0:
      me0+=1
print("A matriz possui",me0,"numero(s) menor(es) que zero.\nA matriz possui",ma0,"numero(s) maior(es) que zero.")
