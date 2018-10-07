p1=[]
p_c= "CINEMA"
p_b= "BOLICHE"
for i in range(0, 7):
 p1.append(input().upper())
c1 = p1.count(p_c)
c2 = p1.count(p_b)
if c1 > c2: 
 print(p_c)
elif c2 > c1: 
 print(p_b)
