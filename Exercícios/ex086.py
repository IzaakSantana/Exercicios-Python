matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha][col] = int(input(f'Digite um valor para [{linha}, {col}]: '))

print('=' * 30)

for l in matriz:
    for num in l:
        print(f'[{num:^5}]', end='')
    print()
