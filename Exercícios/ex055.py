maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa.'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(maior, menor))
