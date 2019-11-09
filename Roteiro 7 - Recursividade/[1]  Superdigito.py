def superDigito(sDigito):
    listDigitos = []
    
    for e in sDigito:
        listDigitos.append(int(e))
        
    sDigito = str(sum(listDigitos))
    
    if len(sDigito) == 1:
        return sDigito
    return superDigito(sDigito)

digito = input().split()
digito = digito[0]*int(digito[1])
print(superDigito(digito))
