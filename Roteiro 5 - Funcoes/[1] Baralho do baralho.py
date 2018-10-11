def Card(cartas):
	pontos=0 # A pontuação no jogo começa com 0 e vai sendo acumulada.
	c = cartas
	c.sort()
	if c[0]+1 == c[1] and c[1]+1 == c[2]: #  +Número da menor carta, se estiverem em ordem crescente com distância 1
		pontos+=c[0]
	if c[0] == c[1] and c[1] == c[2]: # +Número da menor carta, se todas forem iguais
		pontos+=c[0]
	if c[0] == c[1] and c[1] < c[2]: # +Número da menor carta / 2, se existirem apenas duas menores cartas iguais
		pontos+=(c[0]/2)
	if c[1] == c[2] and c[0] < c[2]: # +Número da maior carta / 2, se existirem apenas duas maiores cartas iguais
		pontos+=(c[2]/2)
	if sum(c) == 8: # +8, se a soma das cartas for 8
		pontos+=8
	return pontos
	
def winner(a,b):
	c1=a
	c2=b
	V1=Card(c1) # soma cartas de Paes
	V2=Card(c2) # soma cartas de Willy
	if V1 == V2:
		r=0
	elif V1 > V2:
		r=1
	elif V1 < V2:
		r=2
	return r

c1=[int(i) for i in input().split()]
c2=[int(i) for i in input().split()]

print(winner(c1,c2))
