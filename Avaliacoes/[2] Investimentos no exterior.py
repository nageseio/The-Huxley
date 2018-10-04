# Codigo todo cagado, kkkk
patrimonio_total = float(input())
patrimonio_exterior = float(input())
valor_investido= float(input())
pagou_multa = input()
ppe = valor_investido*0.15
if valor_investido > patrimonio_total*0.2 and patrimonio_exterior >= valor_investido:
    print("Imposto")
    print("%.1f"%ppe)
    print("%.1f"%0)
elif patrimonio_exterior < patrimonio_total*0.2:
   print("Isento")
   print("%.1f"%0)
   print("%.1f"%0)
   quit()
elif patrimonio_total > 1000000 and patrimonio_exterior < valor_investido*0.1:
  print("Imposto+Multa")
  print("%.1f"%ppe)
  print("%.1f"%ppe)
elif patrimonio_total < 1000000 and patrimonio_exterior < valor_investido*0.1:
  print("Imposto")
  print(ppe)
  print("%.1f"%0)
if patrimonio_total >= 1000000 and patrimonio_exterior < valor_investido and pagou_multa == "sim":
  print("Crime")
  print("%.1f"%ppe)
  print("%.1f"%ppe)
elif patrimonio_total >= 1000000 and patrimonio_exterior < valor_investido and pagou_multa == "nao":
  print("Imposto+Multa")
  print("%.1f"%ppe)
  print("%.1f"%ppe)
if valor_investido > patrimonio_total:
  print("Crime")
  print("%.1f"%ppe)
  print("%.1f"%ppe)
