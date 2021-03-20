valor = float(input('Qual o valor do produto? R$'))
print()
pag = int(input('''Qual a forma de pagamento? (digite o número com a opção desejada)

[1] A vista. (dinheiro/cheque) \033[32m10% de desconto\033[m
[2] A vista no cartão. \033[32m5% de desconto\033[m
[3] 2x no cartão. \033[34mpreço normal\033[m
[4] 3x no cartão. \033[33m20% de juros\033[m

'''))
print('\033[36m\n' * 130)
if pag == 1:
    tot = valor - (valor * 10 / 100)
    print('O valor total a pagar será R${}'.format(tot))
elif pag == 2:
    tot = valor - (valor * 5 / 100)
    print('o valor total a pagar será R${}'.format(tot))
elif pag == 3:
    print('O valor a pagar será R${}'.format(valor))
elif pag == 4:
    tot = valor + (valor * 20 / 100)
    print('O valor total a pagar será R${}'.format(tot))
else:
    print('\033[31mOpção inválida')
