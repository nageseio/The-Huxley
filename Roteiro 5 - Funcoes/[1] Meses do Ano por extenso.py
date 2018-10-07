def meses(mes):
  mes = int(mes)
  if mes > 12 or mes < 1:
    me = "invalido"
  else:
    lista_meses=['invalido','janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    me = lista_meses[mes]
  return me
n=int(input())
print(meses(n))
