def par(x,y):
	if x%2 == 0:
		print(x)
	x+=1
	if x != y+1:
		return par(x,y)
x=0
par(x,int(input()))
