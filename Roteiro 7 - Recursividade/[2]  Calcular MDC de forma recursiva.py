def MDC(a,b,c):
    if a == 0 or b == 0:
        return 0
    if a%c == 0 and b%c == 0:
        l.append(c)
    c-=1
    if c == 0:
        if len(l) > 1:
            l.sort()
            return l[-1]
        else:
            return 1
    return MDC(a,b,c)
num1 = int(input())
num2 = int(input())
if num1 > num2:
    co=num2
else:
    co=num1
l=[]
print(MDC(num1,num2,co))
