n=[int(i) for i in input().split()]
lista=[]
l=0
for i in range(0, 3):
 lista.append(n[l])
 l+=1
lista.sort()
print(lista[2],"eh o maior")
