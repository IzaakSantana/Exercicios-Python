soma = 0
tot = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        tot += 1
print()
if tot == 1:
    print('Apenas um número par foi digitado. Não há soma.')
elif tot > 1:
    print('{} númeors pares digitados, a soma entre eles é {}.'.format(tot, soma))
else:
    print('Nenhum número par digitado. Não há soma.')
