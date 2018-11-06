n=int(input())
l=[0]
def Fibonacci(n,a,b):
    if len(l) > n:
        return print(l[n-1])
    a,b = b,a+b
    l.append(a)
    return Fibonacci(n,a,b)
Fibonacci(n,0,1)
