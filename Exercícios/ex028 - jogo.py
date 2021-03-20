from random import randint
from time import sleep

N = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 5...')
sleep(3)
print('-=-' * 20)
R = int(input('Em que número pensei? '))
print('-=-' * 20)
print('PROCESSANDO...')
sleep(2)
print('-=-' * 20)
if R == N:
    print('ACERTOU! Parabéns!')
else:
    print('Número errado! Tente novamente.')
    print('O número pensado foi {}.'.format(N))
