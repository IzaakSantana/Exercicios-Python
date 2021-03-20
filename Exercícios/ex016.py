from math import ceil, floor, trunc

num = float(input('Digite um valor: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))
print('Forma alternativa 1: {}'.format(int(num)))
print('Forma alternativa 2: {:.0f}'.format(num))
