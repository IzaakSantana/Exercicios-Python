titulo = 'Boletim'
print('=' * 27)
print('{:^27}'.format(titulo))
print('=' * 27)
print()
n1 = float(input('Digite a primeia nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Média {}'.format(m))
if m < 5:
    print('\033[31mREPROVADO')
elif 5 < m < 6.9:
    print('\033[33mRECUPERAÇÃO')
elif m >= 7.0:
    print('\033[32mAPROVADO')
