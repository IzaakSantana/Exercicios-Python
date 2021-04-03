# Desafio:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
 
somaPares = soma3aColuna = maior2aLinha = 0

for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha][col] = int(input(f'Digite um valor para [{linha}, {col}]: '))
        valor = matriz[linha][col]
        
        if valor % 2 == 0:
            somaPares += valor

        if col == 2:
            soma3aColuna += valor

        if linha == 1 and valor > maior2aLinha:
            maior2aLinha = valor
            

print('=' * 30)

for l in matriz:
    for num in l:
        print(f'[{num:^5}]', end='')
    print()

print('=' * 30)

print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {soma3aColuna}')
print(f'O maior número da segunda linha é {maior2aLinha}')
