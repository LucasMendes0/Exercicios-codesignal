s1 = "aabcc"
s2 = "adcaa"

def solution(s1, s2):
    lista1 = list(s1)
    lista2 = list(s2)
    iguais = 0

    if len(lista1) > len(lista2):
        maior = lista1.copy()
        menor = lista2.copy()
    elif len(lista1) == len(lista2):
        maior = lista2.copy()
        menor = lista1.copy()
    else:
        maior = lista2.copy()
        menor = lista1.copy()
    
    for c in range(0,len(maior)):
        if maior[c] in menor:
            menor.remove(maior[c]) 
            iguais += 1
            
    return iguais

solution(s1,s2)
