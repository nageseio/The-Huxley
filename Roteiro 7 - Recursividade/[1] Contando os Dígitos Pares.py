def cont(a,b,c):
    if len(a) == b:
        return c
    if a[b]%2 == 0:
        c+=1
    b+=1
    return cont(a,b,c)
c,b=0,0
s=input()
a=[]
for i in range(len(s)):
    a.append(int(s[i]))
print(cont(a,b,c))
