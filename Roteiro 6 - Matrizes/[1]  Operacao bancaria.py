li=[]
while True:
  s=[float(i) for i in input().split()]
  if s[0]==-1:
    break
  else:
    li.append(s)
credito=0
debito=0
for x in range(len(li)):
  for y in range(1):
    if li[x][y] == 1:
      credito+= li[x][1]
    elif li[x][y] == 0:
      debito+= li[x][1]
saldo=credito-debito
print("Creditos: R$ ","%.2f"%credito,"\nDebitos: R$ ","%.2f"%debito,"\nSaldo: R$ ","%.2f"%saldo,sep="")
