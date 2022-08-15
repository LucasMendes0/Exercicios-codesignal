def solution(inputArray):
    cont = 0
    lista = list()

    for c in range(0,len(inputArray)-1):
        lista.append(inputArray[cont]*inputArray[cont+1])
        cont += 1
    print(max(lista))
    return max(lista)

solution([-23, 4, -3, 8, -12])