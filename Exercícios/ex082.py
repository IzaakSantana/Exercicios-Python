lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]

    if resp in 'N':
        break


for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('=' * 50)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
