from datetime import date

A = 0
M = 0

for c in range(1, 8):
    nasc = int(input('Em que ano {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        A += 1
    elif idade < 21:
        M += 1
print()
if A == 0:
    print('Ninguém é maior de idade, todos são menores.')
elif M == 0:
    print('Todos são maiores de idade.')
else:
    print('{} pessoas são maiores de idade, {} são menores.'.format(A, M))
