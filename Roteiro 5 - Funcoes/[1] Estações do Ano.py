def estacao(dia_1_31, mes_1_12):
  p=[10, 11, 12]
  v=[1, 2, 3]
  o=[4, 5, 6]
  i=[7, 8, 9]
  dia = int(dia_1_31)
  mes = int(mes_1_12)
  if mes in p:
    if mes == 12 and dia < 21:
      estacao="PRIMAVERA"
    elif mes == 12 and dia > 20:
      estacao="VERAO"
    else:
      estacao="PRIMAVERA"
  elif mes in v:
    if mes == 3 and dia < 21:
      estacao="VERAO"
    elif mes == 3 and dia > 20:
      estacao="OUTONO"
    else:
      estacao="VERAO"
  elif mes in o:
    if mes == 6 and dia < 21:
      estacao="OUTONO"
    elif mes == 6 and dia > 20:
      estacao="INVERNO"
    else:
      estacao="OUTONO"
  elif mes in i:
    if mes == 9 and dia < 21:
      estacao="INVERNO"
    elif mes == 9 and dia > 20:
      estacao="PRIMAVERA"
    else:
      estacao="INVERNO"
  return estacao

n=input()
n2=input()
print(estacao(n,n2))
