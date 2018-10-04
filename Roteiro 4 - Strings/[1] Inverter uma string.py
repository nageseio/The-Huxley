l=[]
C=-1
n=input()
for i in range(len(n)):
  l.append(n[C])
  C-=1
l = ''.join(l)
print(l)
