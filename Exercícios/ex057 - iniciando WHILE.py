sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while not sexo in 'MF':
    sexo = str(input('Dados inválidos! Digite uma informação válida! > ')).strip().upper()[0]
print('{} registrado com sucesso!'.format(sexo))
