# progressão aritimética

print('=' * 25)
print('{:^25}'.format('10 termos de uma PA'))
print('=' * 25)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pt + 9 * r
for c in range(pt, decimo + r, r):
    print(pt, end=' -> ')
    pt += r
print('Fim')
