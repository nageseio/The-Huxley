l=[]
C=0
n=input()
for i in range(len(n)):
  l.append(n[C])
  C+=1
l.reverse()
l = ''.join(l)
print(int(l))
