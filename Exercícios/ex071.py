print('=' * 30)
print(F'{"BANCO GUANABARA":^30}')
print('=' * 30)

valor = int(input('Qual valor deseja sacar? R$'))
total = valor
cedula = 50
contCed = 0

while True:
    if total >= cedula:
        total -= cedula
        contCed += 1
    else:
        if contCed > 0:
            print(f'{contCed} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contCed = 0
        if total == 0:
            break

print('=' * 30)
print(f'{"Volte sempre!":^30}')
print('=' * 30)