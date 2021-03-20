olderMan = ''
nome = ''
maiorH = menorM = totM = mediaP = idade = 0

for c in range(0, 4):
    print('''
    ============
     {}ª pessoa
    ============
    '''.format(c + 1))   
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))   
    sexo = int(input('Sexo - [1] Masc. | [2] Fem. : '))
    mediaP += idade
    if c == 0:
        olderMan = nome
        maiorH = idade
        menorM = idade
    elif sexo == 1 and idade > maiorH:
        maiorH = idade
        olderMan = nome
    elif sexo == 2 and idade < 20:
        totM += 1

   
mediaF = mediaP / 4

print('''
A média de idade do grupo é {}
O homem mais velho é {} com {} anos.
Há {} mulher(es) com menos de 20 anos.
'''.format(mediaF, olderMan, maiorH, totM))
