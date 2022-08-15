def solution(inputString):
    teste = ""
    cont = -1

    for c in range(0,len(inputString)):
        teste = teste + inputString[cont]
        cont -= 1
        
    if inputString == teste:
        print('Sim')
        return inputString == True
    else:
        print('Não')
        return inputString == False  
    
solution('aabaa')
solution('abac')
solution('a')
    