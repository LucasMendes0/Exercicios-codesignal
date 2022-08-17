def solution(n):
    n = str(n)
    lista = list(n)
    metade = int(len(n)/2)
    metade1 = 0
    metade2 = 0
    
    for c in range(0,metade):
        lista[c] = int(lista[c])
        metade1 += lista[c]
    for c in range(metade,len(lista)):
        lista[c] = int(lista[c])
        metade2 += lista[c]
    
    print(metade1)
    print(metade2) 
    if metade1 == metade2: return True
    else: return False
    
solution(134008)

    