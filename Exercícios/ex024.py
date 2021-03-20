# Programa pra dizer se o nome de uma cidade começa ou não com 'santo'

cidade = str(input('Digite o nome de uma cidade. ')).strip()
print('Começa com "Santo"? {}'.format(cidade[:5].lower() == 'santo'))
