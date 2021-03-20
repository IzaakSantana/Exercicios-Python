# Conversão de numeros

num = int(input('Digite um número inteiro: '))
print()
esc = int(input('''Escolha a base de conversão:

[1] Binário
[2] Octal
[3] Hexadecimal

Sua escolha: '''))
print()
if esc == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
