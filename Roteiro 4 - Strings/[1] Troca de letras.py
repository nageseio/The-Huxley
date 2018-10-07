nu=1
c=0
while c < nu:
  n=[str(i) for i in input()]
  n2 = ''.join(n)
  while "3" in n:
    po = n2.find("3")
    del(n[po])
    n.insert(po, "E")
    n2 = ''.join(n)
  while "4" in n:
    po = n2.find("4")
    del(n[po])
    n.insert(po, "A")
    n2 = ''.join(n)
  while "1" in n:
    po = n2.find("1")
    del(n[po])
    n.insert(po, "I")
    n2 = ''.join(n)
  while "5" in n:
    po = n2.find("5")
    del(n[po])
    n.insert(po, "S")
    n2 = ''.join(n)
  n3 = ''.join(n).upper()
  if n3 == "FIM" or n3 == "SAIR":
    break
  print(''.join(n).upper())
