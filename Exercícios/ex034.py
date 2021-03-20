func = str(input('Qual o nome do funcionário? ')).strip()
salA = float(input('Qual o salário atual de {}? R$'.format(func.split()[0])))
print()
if salA > 1250.0:
    salN = salA + salA * 10 / 100
    A = 10
else:
    salN = salA + salA * 15 / 100
    A = 15
print('\033[32m=\033[m' * 35)
print('''Funcionário: \033[34m{}\033[m
Salário anterior: \033[31m{:.2f}\033[m
Novo salário: \033[32m{:.2f}\033[m
Aumento de \033[33m{}%\033[m'''.format(func, salA, salN, A))
print('\033[32m=\033[m' * 35)
