import random
from time import sleep

vitorias = 0

print('=-=' * 10)
print(f'{"PAR OU ÍMPAR":^27}')
print('=-=' * 10)

while True:
    escolha = str(input('Escolhe PAR ou ÍMPAR? [P/I] ')).strip().upper().replace('í', 'i')[0]
    numUsuario = int(input('Digite um número: '))
    numPC = random.randint(1, 10)
    soma = numUsuario + numPC
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    if escolha == "P":
        escolha == "PAR"
    elif escolha == "I":
        escolha == "ÍMPAR"
    else:
        print('Digite um valor válido!')
    print(f'Você jogou {numUsuario} e o computador jogou {numPC}. Total de {soma}. Deu {resultado}!')
    if resultado == escolha:
        print('Você venceu!\nVamos jogar novamente.')
        vitorias += 1
        sleep(1)
    elif resultado != escolha:
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
