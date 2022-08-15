def solution(year):
    if year % 100 == 0:
        year = str(year)
        print(f'Século {year[0:2]}')
    else:
        print(f'Século {int((year/100) + 1)}')
        
solution(int(input('Insira o ano: ')))        
