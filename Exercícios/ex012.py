# Desafio:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Para calcular a porcentagem faça valor * porcentagem depois resultado / 100.

preco = float(input('Qual é o preço do produto? R$'))
desconto = int(input('Qual é o desconto? %'))
novop = preco - (preco * desconto / 100)
print('O produto que custava R${:.2f} agora com desconto de {}% custa R${:.2f}!'.format(preco, desconto, novop))
