def solution(s):
    index = -1
    #verificou se era uma crescente
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            if index != -1: return False
            index = i
            # se o sucessor for menor que o atual, o index se altera, retornando falso
    # se o valor do index não se alterou, é porque é uma crescente        
    if(index == -1): return True
    
    original = s.copy()
    
    s.pop(index) #caso o primeiro teste encontre um valor problemático
    ok = 1 # variável de controle
    # mesma verificação de antes
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            # se encontrar um valor inválido, altera a variável de controle
            ok = 0
            break
        
    if ok == 1: return True
    
    s = original.copy()
    s.pop(index-1)
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            return False
    return True
    