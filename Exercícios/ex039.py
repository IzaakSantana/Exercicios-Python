from datetime import date

ano_at = date.today().year
titulo = 'Alistamento para o Exército Brasileiro'
print('=' * 50)
print('{:^50}'.format(titulo))
print('=' * 50)
print()
ano_nasc = int(input('Em que ano nasceu? '))
print()
if ano_nasc > ano_at:
    print('\033[31mVocê não pode ter nascido no futuro!')
idade = ano_at - ano_nasc
if idade < 18:
    f = 18 - idade
    if f == 1:
        print('Ainda falta {} ano para você se alistar no exército.'.format(f))
        print('Seu alistamento será em {}.'.format(ano_at + f))
    else:
        print('Ainda faltam {} anos para você se alistar no exército.'.format(f))
        print('Seu alistamento será em {}.'.format(ano_at + f))
elif idade == 18:
    print('Já é hora de se alistar no exército.')
elif idade > 18:
    p = idade - 18
    if p == 1:
        print('Você deveria ter se alistado em {}.'.format(ano_at - p))
    else:
        print('Você deveria ter se alistado em {}.'.format(ano_at - p))
