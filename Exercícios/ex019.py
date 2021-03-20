# Sorteio pra apagar o quadro.
from random import choice

print('Digite o nome dos quatro alunos: ')
A1 = input('1: ')
A2 = input('2: ')
A3 = input('2: ')
A4 = input('4: ')
lista = [A1, A2, A3, A4]
escolhido = choice(lista)
print('O aluno sorteado foi {}!'.format(escolhido, ))
