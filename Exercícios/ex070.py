print('=' * 35)
print(f'{"LOJA PREÇO BOM":^35}')
print('=' * 35)

totCompra = maior1k = MaisBarato = cont = 0
ProdMaisBarato = ''

while True:
    produto = str(input('\nNome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    totCompra += preço

    if cont == 1 or preço < MaisBarato:
        MaisBarato = preço
        ProdMaisBarato = produto

    if preço > 1000:
        maior1k += 1
    

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer contiunuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{" FIM DO PROGRAMA ":=^35}')

print(f'''
O total gasto na compra foi: R${totCompra:.2f}
Produtos que custaram mais de R$1000.00: {maior1k}
O produto mais barato foi {ProdMaisBarato} que custou R${MaisBarato:.2f}
''')
