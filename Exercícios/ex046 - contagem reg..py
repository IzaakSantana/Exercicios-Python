from time import sleep

print('\033[30m=' * 50)
print('{:^50}'.format('Reveillion 2020!'))
print('=' * 50)
print()
print('Começando contagem...')
sleep(1)
print('\033[33m')
for c in range(10, 0, -1):
    print('\033[1;33m{}!'.format(c))
    sleep(1)
print('\033[1;32m{:^10}'.format('FELIZ ANO NOVO!'))
