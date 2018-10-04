x = int(input())
lista = [int(x) for x in input().split()]
n_min = min(lista)
n_pos = lista.index(n_min)
print("Menor valor:",min(lista))
print("Posicao:",n_pos)
