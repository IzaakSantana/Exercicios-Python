from math import factorial

escolha = int(input('''1 - Minha versão
2 - módulo math
3 - Versão do Guanabara
> '''))

if escolha == 1: # minha versão (tradicional)
    numero = int(input('Digite um número pra saber seu fatorial: '))
    produto = numero
    print(f'Calculando: {numero}! = ', end='')
    while numero != 1:       
        print(f'{numero} x ' if numero != 1 else f'{numero} = {produto} ', end='')       
        numero -= 1
        produto *= numero
        if numero == 1:
            print(f'{numero} = {produto}')
            
elif escolha == 2: # versão do Guanabara (módulo math)
    numero = int(input('Digite um número para saber seu fatorial: '))
    f = factorial(numero)
    print(f'O fatorial de {numero} é {f}')

else: # versão do Guanabara (tradicional)
    numero = int(input('Digite um número para saber seu fatorial: '))
    contador = numero
    fatorial = 1
    print('Calculando: {}! = '.format(numero), end='')
    while contador > 0:
        print('{}'.format(contador), end='')
        print(' x ' if contador > 1 else ' = ', end='')
        fatorial *= contador
        contador -= 1
    print('{}'.format(fatorial))
