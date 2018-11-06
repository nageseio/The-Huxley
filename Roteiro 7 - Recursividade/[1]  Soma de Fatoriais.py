l=[]
for i in range(5):
    l.append(int(input()))
c=0
s=1
ss=0
def Soma(li,c,s,ss):
    if len(li) == c:
        return ss
    if li[c]%3 == 0:
        for i in range(1,li[c]+1):
            s=s*i
        ss+=s
        c+=1
        s=1
    else:
        c+=1
    return Soma(li,c,s,ss)
print(Soma(l,c,s,ss))
