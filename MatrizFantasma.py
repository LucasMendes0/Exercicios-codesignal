#somar apenas os valores que não possuem 0 acima

matriz = [[1,0,3],
          [0,2,1],
          [1,2,0]]

# [0][0],[0][1],[0][2],[0][3]
# [1][0],[1][1],[1][2],[1][3]
# [2][0],[2][1],[2][2],[2][3]


# [2][0] - [1][0] 
# [2][2] - [1][2]
# [2][3] - [1][3]

# [i][x] - [i-1][x], O segundo índice é igual e o primeiro é -1

def solution(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 and matriz[i][j] != 0:
#                print(f'Soma do elemento {j} da matriz {i} ---------- {matriz[i][j]}')
                soma += matriz[i][j]
            elif i == 1 and matriz[i-1][j] != 0 and matriz[i][j] != 0:
                print(f'Soma do elemento {j} da matriz {i} ---------- {matriz[i][j]}')
                soma += matriz[i][j]
            elif i == 2 and matriz[i-1][j] != 0 and matriz[i-2][j] !=0 and matriz[i][j] != 0:
                print(f'Soma do elemento {j} da matriz {i} ---------- {matriz[i][j]}')
                soma += matriz[i][j]
    print(soma)
    return soma
solution(matriz)



