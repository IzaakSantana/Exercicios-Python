numeros = [[], []]

temp = 0

for c in range(1, 8):
    temp = int(input(f'Digite o {c}º valor: '))

    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)

numeros[0].sort()
numeros[1].sort()
print('=' * 70)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
