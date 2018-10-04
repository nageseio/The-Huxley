l=0
l2=1
ni=int(input())
for i in range(0,ni):
  n=[str(i) for i in input()]
  for i in range(len(n)):
    if l2 < len(n):
      if n[l] != n[l2]:
        l+=1
        l2+=1
      else:
        del(n[l2])
  l=0
  l2=1
  n = ''.join(n)
  print(n)
