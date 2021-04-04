# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = []
temp = []

print("=" * 20)
print(f"{'MEGA SENA':^20}")
print("=" * 20)

xJogos = int(input("Quantos jogos você quer sortear? "))
print('\n', '=' * 10, f'SORTEANDO {xJogos} jogos', '=' * 10)
print()

for j in range(0, xJogos): # cria as temps
    temp.clear()
    for n in range(0, 6): # adiciona valores nelas
        randNum = randint(1, 60)

        if not randNum in temp:
            temp.append(randNum)
        else:
            temp.append(randint(1, 60))
    
    temp.sort()
    jogos.append(temp[:])

for ind, val in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {ind+1}: {val}')

print()
print('=' * 10, f'BOA SORTE!', '=' * 10)
