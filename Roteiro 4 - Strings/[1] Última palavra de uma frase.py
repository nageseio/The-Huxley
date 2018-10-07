C=1
li=[]
l=-1
n=[str(i) for i in input()]
if " " in n:
  while 0 < C:
    if n[l] != " ":
      li.append(n[l])
    l-=1
    if n[l] == " ":
      break
  li.reverse()
  print(''.join(li))
else:
  print(''.join(n))
