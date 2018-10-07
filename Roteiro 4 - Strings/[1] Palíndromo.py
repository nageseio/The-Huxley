n=int(input())
lii=[]
cm=-1
c=0
while c < n:
  nn=[str(i) for i in input().upper()]
  while " " in nn:
   nn.remove(" ")
  li=nn[:]
  for i in range(0, len(nn)):
    lii.append(nn[cm])
    cm-=1
  if li == lii:
    print("SIM")
  else:
    print("NAO")
  lii=[]
  c+=1
  cm=-1
