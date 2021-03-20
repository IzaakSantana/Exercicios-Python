matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for linha, linVal in enumerate(matriz):
    for col, colVal in enumerate(linVal):
        linVal[col] = int(input(f'Digite um valor para [{linha}, {col}]: '))

print('=' * 30)

for l in matriz:
    for num in l:
        print(f'[{num:^5}]', end='')
    print()
