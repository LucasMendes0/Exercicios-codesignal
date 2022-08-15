def solution(sequence):
    cont = 0
    teste = list()
    n = 0
    if len(sequence) == 1:
        return True
    elif len(sequence) == 2 and sorted(sequence) == sequence:
            return True
    else:
        while n < len(sequence):
            if sequence[n] not in teste:
                teste.append(sequence[n])
                n += 1
            else:
                if cont == 1:
                    teste.append(sequence[n])
                    n += 1
                    cont+=1
                else:
                    return False
    print(teste)
    print(sequence)
    print(sorted(teste))
    print(sorted(sequence))
    
    if teste == sequence:
        nomax = teste.copy()
        nomax.remove(max(nomax))
        nomin = teste.copy()
        nomin.remove(min(nomin))
        nopop = teste.copy()
        nopop.pop()
        
        if sorted(nomax) == nomax:
            print('True no max')
            return True
        elif sorted(nomin) == nomin:
            print('True nomin')
            return True
        elif sorted(nopop) == nopop:
            print('True nopop')
            return True
        else:
            print('False nomax nomin')
            return False
        
        print()
    
    
    if cont >= 2 or teste != sorted(sequence):
        print('False')
        return False
    else:
        print('True')
        return True