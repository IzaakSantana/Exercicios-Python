# Desafio:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Quantos reais você tem? R$'))
cotacaoD = float(input('Qual o valor do dólar atual? '))
cotacaoE = float(input('Qual o valor do euro? '))
cotacaoB = float(input('Qual o valor do bitcoin? '))
dolares = reais / cotacaoD
euro = reais / cotacaoE
bitcoin = reais / cotacaoB
print('\nCom R${:.2f} você pode comprar U${:.2f} dólares, £{:.2f} euros e {:.2f} bitcoins!'.format(reais, dolares, euro, bitcoin))
