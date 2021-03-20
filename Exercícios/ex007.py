# Desafio:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
M = (N1 + N2) / 2
print('A média é {:.1f}'.format(M))
