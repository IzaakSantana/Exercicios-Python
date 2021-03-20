# R$0.50 viagens de até 200Km, R$0.45 viagens com mais de 200Km.

cores = {'magenta': '\033[35m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'limpa': '\033[m'}
destino = str(input('\033[34mQual o destino da viagem? ')).strip()
dis = float(input('Qual a distância em Km? '))
if dis <= 200:
    passagem = 0.50 * dis
else:
    passagem = 0.45 * dis
print()
print('=' * 30)
print('''Destinho: {}{}{}
Distância: {}{:.1f}Km{}
Valor da passagem: {}R${:.2f}{}'''.format(cores['magenta'], destino, cores['azul'], cores['magenta'], dis, cores['azul'], cores['amarelo'], passagem, cores['azul']))
print('=' * 30)
