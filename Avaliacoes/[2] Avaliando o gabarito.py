b,pontos,l,l2,l3,c,qnt,qnt_a,qnt3,pg=1,0,0,0,0,0,0,0,0
listan=[]
gabarito=[str(i) for i in input()]
while b>0:
  nome_a = input()
  qnt_a+=1
  if nome_a == "sair":
    break
  notas=[str(i) for i in input()]
  for i in range(0,5):
    if gabarito[l] == notas[l2]:
      pontos+=20
    l+=1
    l2+=1
  listan.append(pontos)
  pg+=pontos
  if pontos > 60:
    qnt+=1
  if pontos >= c:
    n1 = nome_a
    c = pontos
  media_g = pg/qnt_a
  pontos=0
  l=0
  l2=0
for i in range (0, qnt_a-1):
  if media_g < listan[l3]:
    qnt3+=1
  l3+=1
print(qnt3)
print(n1)
