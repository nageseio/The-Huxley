l=1
C=-1
l2=-1
str2=[]
li=[]
n=[str(i) for i in input().split()]
if len(n)%2 ==0:
  le = len(n)-1
elif len(n)%2 ==1:
  le = len(n)-1
for i in range(0, le, 2):
  str1 = ''.join(n[l])
  v = len(str1)
  for i in range(v):
    li.append(str1[C])
    C-=1
  lii = ''.join(li)
  n[l] = lii
  C=-1
  li=[]
  l+=2
n = ' '.join(n)
print(n)
