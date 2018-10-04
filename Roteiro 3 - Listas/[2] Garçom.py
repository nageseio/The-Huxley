bandejas=0
copos_q=0
n=int(input())
while bandejas < n:
  lista = [int(i) for i in input().split()]
  if lista[0] > lista[1]:
    copos_q = copos_q + (lista[1])
  bandejas+=1
print(copos_q)
