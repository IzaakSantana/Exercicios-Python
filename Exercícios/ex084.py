pessoas = list()
dados = list()
pesadas = list()
leves = list()
maiorPeso = menorPeso = 0
txtPesadas = txtLeves = ''

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

for c in range(0, len(pessoas)):
    nome = pessoas[c][0]
    peso = pessoas[c][1]

    if c == 0:
        maiorPeso = menorPeso = peso
        pesadas.append(nome)
        leves.append(nome)
    
    elif peso > maiorPeso:
        maiorPeso = peso 
        pesadas.clear()
        pesadas.append(nome)
    
    elif peso < menorPeso:
        menorPeso = peso 
        leves.clear()
        leves.append(nome)

    elif peso == maiorPeso:
        pesadas.append(nome)

    elif peso == menorPeso: 
        leves.append(nome)

for pessoa in leves:
    txtLeves += f'[{pessoa}] '

for pessoa in pesadas:
    txtPesadas += f'[{pessoa}] '

print('-=' * 20)
print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi {maiorPeso} de: {txtPesadas}')
print(f'O menor peso foi {menorPeso} de: {txtLeves}')
