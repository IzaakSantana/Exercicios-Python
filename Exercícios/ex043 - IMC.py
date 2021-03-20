# Calcula o IMC

print('=' * 50)
print('{:^50}'.format("Bem vindo ao calculador de IMC!"))
print('=' * 50)
print()

c = 0
nome = str(input('Digite seu nome:\n')).strip().title()
peso = float(input('Informe seu peso: (Kg)'))
altura = float(input('informe sua altura: (m) '))
imc = peso / (altura * altura)

print('\n' * 130)
print('Ficha:\n')
print(f'Nome: {nome}')
print(f'Peso: {peso}')
print(f'Altura: {altura:.2f}')
print(f'IMC (índice de massa corporal): {imc:.1f}Kg/m²')
print()

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está dentro do peso adequado!')
elif 25 <= imc < 30:
    print('Você está acima do peso!')
elif 30 <= imc < 40:
    print('Você está em estado de obesidade!')
elif imc > 40:
    print('Você está em estado de obesidade mórbida!')
