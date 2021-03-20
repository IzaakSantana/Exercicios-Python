print('=' * 25)
print(f'{"10 termos de uma PA":^25}')
print('=' * 25)

pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 9
print()
print(f'{pt}', end=' -> ')
while c > 0:
    pt += razão
    print(f'{pt} -> ' if c > 1 else f'{pt}', end='')
    c -= 1
print()
