lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

print('=' * 50)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições: ', end='')

if lista.count(max(lista)) > 1:
    for pos, num in enumerate(lista):
        if num == max(lista):
            print(f'{pos}...', end=' ')
else:
    print(f'{lista.index(max(lista))}...', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições: ', end='')

if lista.count(min(lista)) > 1:
    for pos, num in enumerate(lista):
        if num == min(lista):
            print(f'{pos}...', end=' ')
else:
    print(f'{lista.index(min(lista))}...')

print()
