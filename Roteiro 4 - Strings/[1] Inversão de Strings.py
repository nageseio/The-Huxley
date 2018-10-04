n=int(input())
l=-1
for i in range(0,n):
  no=input()
  for i in range(len(no)):
    print(no[l],end="")
    l-=1
  print("")
  l=-1
