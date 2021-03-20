from os import system

cmd = system
maioresDe18 = homensCad = mulherMen20 = 0
titulo = 'CADASTRE UMA PESSSOA'
num = len(titulo) + 2

while True:
    print('=' * num)
    print(f'{titulo:^22}')
    print('=' * num)
    idade = int(input('\nIdade: '))
    sexo = ' '

    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if idade >= 18:
        maioresDe18 += 1
    if sexo == 'M':
        homensCad += 1
    elif idade < 20:
        mulherMen20 += 1
    
    resp = ' '
    while resp not in "SN":
        print('-' * num)
        resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
        print('-' * num)
    if resp == 'N':
        break
    cmd('cls')

print(f'''
Pessoas maiores de 18 anos: {maioresDe18}
Homems cadastrados: {homensCad}
Mulheres com menos de 20 anos: {mulherMen20}
''')
