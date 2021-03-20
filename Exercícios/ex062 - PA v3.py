print('=' * 20)
print(f'{"Gerador de PA":^20}')
print('=' * 20)

pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 1
total = 0
mais = 10
print()
while mais != 0:
    total += mais
    while c <= total:
        print(f'{pt} -> ', end='')
        pt += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f"Progressão finalizada com {total} termos mostrados.")
