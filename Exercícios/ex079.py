lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    
    resp = str(input('Quer continuar? [S/N] '))[0].strip().upper()

    if resp == 'N':
        break

print('=' * 50)
lista.sort()
print(f'Você digitou os valores {lista}') # ou sorted(lista)
