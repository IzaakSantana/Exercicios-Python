

from random import randint
from time import sleep

jogos = []

print("=" * 20)
print(f"{'MEGA SENA':^20}")
print("=" * 20)

xJogos = int(input("Quantos xJogos você quer sortear? "))
print('\n', '=' * 10, f'SORTEANDO {xJogos} xJogos', '=' * 10)

for j in range(0, xJogos): # cria as temps
    temp = []
    for n in range(0, 6): # adiciona valores nelas
        sleep(0.1)
        randNum = randint(1, 60)

        if not randNum in temp:
            temp.append(randNum)
            temp.sort()
        else:
            temp.append(randint(1, 60))
            temp.sort()
    lista.append(temp[:])
    print(f'Jogo {j+1}: {temp}')
print('=' * 10, f'BOA SORTE!', '=' * 10)

# INCOMPLETO (dps termina de ver o vídeo)