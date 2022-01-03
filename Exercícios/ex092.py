# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
#  além da idade, com quantos anos a pessoa vai se aposentar.
from time import strftime

anoAtual = int(strftime('%Y'))
anosParaAposentadoria = 35

trabalhador = {}

trabalhador['nome'] = input("Digite seu nome: ").strip().title()
trabalhador['nascimento'] = int(input("Ano de nascimento: "))
trabalhador['ctps'] = int(input("Carteira de Trabalho (0 se não tem): "))
trabalhador['idade'] = anoAtual - trabalhador['nascimento']

if trabalhador['ctps'] != 0:
    trabalhador['anoDeContrato'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = float(input("Salário: "))
    trabalhador['aposentadoria'] = trabalhador['anoDeContrato'] 
    - trabalhador['nascimento'] + 35

print("=" * 30)

for key, value in trabalhador.items():
    print(f"{key} tem o valor: {value}")
