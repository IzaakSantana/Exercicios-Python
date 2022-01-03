# Desafio: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

jogadores = dict()
ranking = list()

for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)


print('Valores sorteados:')

for chave, valor in jogadores.items():
    sleep(0.6)
    print(f'{chave} tirou {valor} no dado.')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\n=== RANKING ===\n')

for chave, valor in enumerate(ranking):
    sleep(0.6)
    print(f'{chave + 1}º lugar: {valor[0]} com {valor[1]}')
