def CalculaHospedagem(ho,dia):
  ind=125
  sd=140
  st=180
  r=0
  if ho == "individual":
    r = ind*dia 
  elif ho == "suíte dupla" or ho == "suítedupla" or ho == "suitedupla" or ho == "suite dupla":
    r = sd*dia
  elif ho == "suíte tripla" or ho == "suítetripla" or ho == "suite tripla" or ho == "suitetripla":
    r = st*dia
  if dia > 2:
    r = r*0.85
  return r
ho=input().lower()
dia=int(input())
print("%.2f"%CalculaHospedagem(ho,dia))
