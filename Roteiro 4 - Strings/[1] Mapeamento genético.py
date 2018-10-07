dna=input()
dna2=input()
li=[]
cc=2
if dna2 in dna:
  while cc <  99:
    if 0 in li:
      break
    c1 = dna.count(dna2*cc)
    li.append(c1)
    cc+=1
else:
  print("ERRO")
if len(li) > 1:
  cc = cc-2
  print(dna.find(dna2*cc))
  print(len(li)) 
elif len(li) == 1:
 print(0)
 print(1)
