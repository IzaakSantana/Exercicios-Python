extensos = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {extensos[num]}')
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
        if resp in 'n':
            break


