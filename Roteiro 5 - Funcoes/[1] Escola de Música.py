def ClassificaAluno(media,q_faltas):
  if media >= 9.5 and q_faltas < 11:
    resultado = "APROVADO COM LOUVOR"
  elif media >= 7:
    if q_faltas < 11:
      resultado = "APROVADO"
    elif q_faltas > 10:
      resultado = "REPROVADO POR FALTAS"
  elif media < 7:
    resultado = "REPROVADO"
  return resultado
media=float(input())
q_faltas=int(input())
print(ClassificaAluno(media,q_faltas))
