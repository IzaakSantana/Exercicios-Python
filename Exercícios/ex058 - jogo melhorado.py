from random import randint
from time import sleep
from os import system
import prompt

acertou = False
palpite = tentativas = 0
pcNum = randint(0, 10)
print()
print('Eu vou pensar em um número de 0 à 10. Adivinhe qual!')
while not acertou:
    print()
    palpite = int(input('Seu palpite: '))
    if palpite != pcNum:
        tentativas += 1
        print('Número errado! ', end='')
        if palpite > pcNum:
            print('Digite um número menor.')
        else:
            print('Digite um número maior.')
    elif palpite == pcNum and tentativas == 0:
        acertou = True
        prompt.cls()
        print('Parabéns!!! Você acertou de primeira!')
    else:
        acertou = True
        prompt.cls()
        if tentativas == 1:
            print('Parabéns!!! Você acertou, mas errou {} vez.'.format(tentativas))
        else:
            print('Parabéns!!! Você acertou, mas errou {} vezes.'.format(tentativas))
