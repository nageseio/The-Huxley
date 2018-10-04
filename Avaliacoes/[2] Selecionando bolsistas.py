x=0
ecp=0
tel=0
bolsista_n=0
n_aluno2=0
soma2=0
while x >= 0:
  n_aluno=input()
  if n_aluno == "sair":
    break
  curso=input()
  periodo=int(input())
  simnao=input()
  cre=float(input())
  recomendacao=int(input())
  if curso == "EC": 
    if periodo > 2:
      if simnao == "sim":
        ecp+=50 
  elif curso == "TEL":
    if periodo > 1:
      if simnao == "sim":
        tel+=50 
  recomendacao = recomendacao*10
  soma=recomendacao+cre+ecp+tel
  if soma > soma2:
    n_aluno2 = n_aluno
    soma2 = soma
  ecp=0
  tel=0
print("O bolsista serah:",n_aluno2)
