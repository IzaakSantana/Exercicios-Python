# Dólar: 3.86 - Euro: 4.31 Bitcoin: 34829.86

reais = float(input('Quantos reais você tem? R$'))
cotacaoD = float(input('Qual o valor do dólar atual? '))
cotacaoE = float(input('Qual o valor do euro? '))
cotacaoB = float(input('Qual o valor do bitcoin? '))
dolares = reais / cotacaoD
euro = reais / cotacaoE
bitcoin = reais / cotacaoB
print('\nCom R${:.2f} você pode comprar U${:.2f} dólares, £{:.2f} euros e {:.2f} bitcoins!'.format(reais, dolares, euro, bitcoin))
