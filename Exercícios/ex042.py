# Triangulo

msg = 'ANALISADOR DE TRIÂNGULOS'
print('\033[33m=' * 35)
print('\033[33m{:^35}'.format(msg))
print('\033[33m=\033[m' * 35)
A = float(input('Informe o primeiro seguimento (cm): '))
B = float(input('Informe o segundo seguimento (cm): '))
C = float(input('Informe o terceiro seguimento (cm): '))
print()
if A < B + C and B < C + A and C < A + B:
    print('Estes seguimentos podem formar um triângulo!')
    if A == B and A == C:
        print('É um triângulo equilátero.')
    elif A != B != C != A:
        print('É um triângulo escaleno.')
    else:
        print('É um triângulo isósceles.')
else:
    print('Estes seguimentos não podem formar um triângulo!')
