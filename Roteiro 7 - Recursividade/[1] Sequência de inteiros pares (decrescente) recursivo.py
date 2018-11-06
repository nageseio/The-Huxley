def par(x,y):
	if x%2 == 0:
		l.append(x)
	if x != y:
		x+=1
		return par(x,y)
	if x == y:
		for i in range(1,len(l)+1):
			print(l[-i])
x=0
l=[]
par(x,int(input()))
