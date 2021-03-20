print('Digite quatro números: ')
tupla = (int(input("1: ")), int(input("2: ")), int(input("3: ")), int(input("4: ")))

x9 = tupla.count(9)
pares = []

if 3 in tupla:
    pos3 = tupla.index(3) + 1
    msg = f"O valor 3 foi digitado na {pos3}ª posição."
else:
    msg = "O valor 3 não foi digitado em nenhuma posição."

for num in tupla:
    if num % 2 == 0:
        pares += [num]


print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {x9} vezes.')
print(msg)

if len(pares) > 0:
    print("Os valores pares digitados foram: ", end='')
    for c in pares:
        print(c, end=' ')
else:
    print('Nenhum valor par foi digitado.')
