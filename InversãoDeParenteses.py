# identificar quando aparecer parenteses
# identificar tudo o que está dentro dele
# inverter e devolver

def solution(texto):
       
    texto2 = list(texto) #transforma em lista para inverter
    aberto = [] # verificador
       
    for i,c in enumerate(texto2):
        if c == '(':
            aberto.append(i) 
        elif c == ')':
            j = aberto.pop() # entendi a inversão, mas não sei porque j recebeu um pop
            texto2[j:i] = texto2[i:j:-1] # esse método só é possível se for em uma lista
            
    return ''.join(c for c in texto2 if c not in '()')
    # eu não faço a menor ideia de como essa linha funciona
    # mas copiei de um vídeo e submeti porque já estava há muito tempo
    # sem ter a menor ideia de como resolver esse problema

solution ("foo(bar(baz))blim")
