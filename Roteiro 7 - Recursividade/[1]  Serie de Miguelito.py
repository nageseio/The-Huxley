def SerieMiguelito(x,c):
	if len(l) > x:
		g =(l[x-1])
		return print(g)
	l.append(c)
	c+=4
	l.append(c)
	c+=1
	return SerieMiguelito(x,c)

l=[]
c=3
SerieMiguelito(int(input()),c)
