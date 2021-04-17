# Desafio Faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Média < 7: recuperação, média < 5: reprovado

aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 7 and aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'


print('=' * 50)

for chave, valor in aluno.items():
    print(f' - {chave}: {valor}')
