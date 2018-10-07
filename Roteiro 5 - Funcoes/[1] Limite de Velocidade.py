def CalculaMulta(kmh):
  if kmh <= 50:
    resultado=0
  elif kmh > 50 and kmh < 56:
     resultado=230
  elif kmh > 55 and kmh < 61:
      resultado=340
  elif kmh > 60:
    resultado = (kmh-50)*19.28
  return resultado
kmh=float(input())
print("%.2f"%CalculaMulta(kmh))
