from datetime import date

ano_at = date.today().year
ano_nas = int(input('Em que ano nasceu o atleta? '))
idade = ano_at - ano_nas
print()
categoria = ''
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print('O atleta é de categoria {}.'.format(categoria))
