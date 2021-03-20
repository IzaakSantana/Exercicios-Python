sn = "S"
cont = maior = menor = total = 0

while sn == "S":
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    sn = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
média = total / cont
print(f'''A média entre todos os números digitados é {média:.2f}
O maior número digitado foi {maior} e o menor foi {menor}''')
