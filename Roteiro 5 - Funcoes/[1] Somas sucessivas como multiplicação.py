def SomasSucessivas(v1,v2):
  resultado = 0
  if v2 > 0:
    for i in range(0,v2):
      resultado+=v1
    return resultado
  elif v2 < 0:
    for i in range(0,abs(v2)):
      resultado-=v1
  elif v1 == 0 or v2 == 0:
    resultado = 0
  return resultado
v1=int(input())
v2=int(input())
print(SomasSucessivas(v1,v2))
