msg = 'ANALISADOR DE TRIÂNGULOS'
print('\033[33m=' * 35)
print('\033[33m{:^35}'.format(msg))
print('\033[33m=\033[m' * 35)
A = float(input('Informe o primeiro seguimento (cm): '))
B = float(input('Informe o segundo seguimento (cm): '))
C = float(input('Informe o terceiro seguimento (cm): '))
print()
if A < B + C and B < C + A and C < A + B:
    print('Estes seguimentos \033[32mpodem\033[m formar um triângulo!')
else:
    print('Estes seguimentos \033[31mnão\033[m podem formar um triângulo!')
if A == B and A == C:
    print('É um \033[35mtriângulo equilátero.')
