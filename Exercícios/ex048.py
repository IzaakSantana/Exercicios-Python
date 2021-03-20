impar = ''
totim = 0
soma = 0
notm = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        totim += 1
    elif c % 2 != 0 and c % 3 != 0:
        notm += 1
print('''Em um intervalo de 1 até 500, a soma entre
todos os números ímpares múltiplos de 3 é: {}
Houve um total de {} números ímpares, {} deles
não são múltiplos de 3.'''.format(soma, totim, notm))
