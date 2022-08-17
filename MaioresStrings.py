lista = ["aba", "aa", "ad", "vcd", "aba"]

def solution(lista):
    teste = 0
    maior = 0
    maiores = list()
    
    
    for c in range(len(lista)):
        teste = len(lista[c])
        if teste > maior:
            maior = teste
        print(maior)
    
    for c in range(len(lista)):
        if len(lista[c]) == maior:
            maiores.append(lista[c])
    
    return maiores
    
solution(lista) 
