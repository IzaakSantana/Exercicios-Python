from random import randint
 
r = randint

numeros = (r(1, 9), r(1, 9), r(1, 9), r(1, 9), r(1, 9))

print("Os númeors sorteados foram: ", end='')

for c in numeros:
    print(c, end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
