from prompt import cls

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opc = 0
cls()
while opc != 5:
    print('''
Ações
    
[1] somar
[2] multiplicar
[3] mostrar o maior
[4] novos números
[5] sair do programa
''')
    opc = int(input('>>> '))
    if opc == 1:
        cls()
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opc == 2:
        cls()
        print('O produto de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            cls()
            print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            cls()
            print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
        else:
            cls()
            print('Os dois são iguais.')
    elif opc == 4:
        cls()
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite o segundo: '))
    elif opc == 5:
        break
    else:
        cls()
        print('Opção inválida!')
