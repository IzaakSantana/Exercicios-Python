# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
# notas de cada aluno individualmente.

alunos = list()
aluno = list()
notas = list()

while True:
    aluno.append(input('Nome: ').strip().title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    media = (notas[0] + notas[1]) / 2
    aluno.append(media)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()

    resp = input("Quer continuar? [S/N] ")[0].upper()
    if resp == 'N':
        break

print('=' * 30)

# 4, 13, 4
print(f'No. {"NOME":<13} MÉDIA')
print('-' * 30)

for ind, val in enumerate(alunos):
    print(f'{ind:<3} {val[0]:<13} {val[1]:>4.1f}')

print('-' * 60)

while True:
    resp = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))

    if resp == 999:
        break
    elif resp <= len(alunos) - 1:
        print(f'Notas de {alunos[resp][0]}: {alunos[resp][2]}')
        print('-' * 30)

print('- Finalizado -')
