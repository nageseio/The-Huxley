l=['0','1','2','3','4','5','6','7','8','9']
n=input()
if len(n) > 6:
  l[6] = n[6]
  l = ''.join(l)
  if l[6] == "b":
    print("Bulbassauro")
  elif l[6] == "c":
    print("Charmander")
  elif l[6] == "s":
    print("Squirtle")
  else:
    print("Codigo Invalido")
else:
  print("Codigo Invalido")
