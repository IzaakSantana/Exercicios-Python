colocados = (
    'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
    'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG',
    'Fluminense', 'Botafogo', 'Cerá SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
)

primeiros5 = colocados[0:5]
ultimos4 = colocados[-4:]
timesOrdenados = sorted(colocados)
pos_chapecoense = colocados.index('Chapecoense') + 1
linhas = '=' * 35

print(linhas)
print(f'{"Lista de times do brasileirão: (2019)":^35}')
print(f'{linhas}\n')

for pos, times in enumerate(colocados):
    pos += 1
    print(f'| {pos} - {times}')

print(f'\n{linhas}')
print(f'{"Primeiros cinco colocados:":^35}')
print(linhas, '\n')

for c in primeiros5:
    print(f'|{c}')

print(f'\n{linhas}')
print(f'{"Últimos quatro colocados:":^35}')
print(linhas, '\n')

for c in ultimos4:
    print(f'|{c}')

print(f'\n{linhas}')
print('Todos os times em ordem alfabética:')
print(f'{linhas}\n')

for time in timesOrdenados:
    print(f'|{time}')

print(f'\n{linhas}')
print(f'{f"Posição do time Chapecoense: {pos_chapecoense}":^35}')
print(f'{linhas}\n')
