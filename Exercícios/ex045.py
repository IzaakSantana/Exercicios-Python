# https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura link - turorial Jokenpo

from os import system
from time import sleep
import random

cmd = system
venceu = '\033[32mPARABÉNS! Você venceu!\033[m'
perdeu = '\033[33mEu venci!\033[m'
lista = ['pedra', 'papel', 'tesoura']
sab = str(input('Você sabe jogar Jokempô? (sim/não)')).strip().lower().split()[0]
keepp = 'sim'
if sab == 'sim' or sab == 's' or sab == 'claro' or sab == 'sei':
    print('Então vamos jogar!')
else:
    print('Veja seu navegador.')
    cmd('start https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura')
sleep(0.5)
print('Iniciando em:')
sleep(0.2)
print('3...', end=' ')
sleep(1)
print('2...', end=' ')
sleep(1)
print('1...')
sleep(0.5)
print('\n' * 130)
while keepp == 'sim' or keepp == 's':
    print()
    escolha = str(input('''\033[36mQual você escolhe?
\033[30m
Pedra
Papel
Tesoura
\033[m
''')).strip().lower()
    pc = random.choice(lista)
    print('\033[33m{}'.format(pc))
    print()
    if escolha == 'pedra' and pc == 'tesoura':
        print(venceu)
    elif escolha == 'tesoura' and pc == 'papel':
        print(venceu)
    elif escolha == 'papel' and pc == 'pedra':
        print(venceu)
    elif escolha == 'tesoura' and pc == 'pedra':
        print(perdeu)
    elif escolha == 'papel' and pc == 'tesoura':
        print(perdeu)
    elif escolha == 'pedra' and pc == 'papel':
        print(perdeu)
    elif escolha == pc:
        print()
        print('\033[33mHouve um empate!')
    else:
        print()
        print('\033[31mOpção inválida!')
    print()
    keepp = str(input('\033[36mDeseja jogar novamente? (sim/não)')).strip().lower()
print()
print('\033[34mObrigado por jogar! Até a próxima!')
