a = [-1, 150, 190, 170, -1, -1, 160, 180]
b = [2,1,3]

# substituir se x > y, exceto se x = -1


def solution(a):
    
    indices = list()
    lista = list()
    
    for c in range(0,len(a)):
        if a[c] == -1:
            indices.append(c)
        else:
            lista.append(a[c])
            
    lista.sort()
    
    for c in range(0,len(indices)):
        lista.insert(indices[c],-1)    
    return a
    

solution(a)    
    
# a[c-1] > a[c]
# a[c] vira a[c-1]
# a[c-1] vira a[c]    
    
    
#        elif a[c] != 0:
#            if a[c] > maior:
#                maior = a[c]
#            if a[c] < menor:
#                menor = a[c]
                    