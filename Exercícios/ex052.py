n = int(input("Digite um número inteiro: "))
d = 0  # divisível

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m{}\033[m'.format(c), end=' ')
        d += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if d == 2:
    print('\nO número {} é divisível apenas por 1 e ele mesmo, por isso é um número primo!'.format(n))
elif d ==1:
    print('\nO número 1 não é primo!')
elif n == 0:
    print('\nZero não é um número primo!')
else:
    print('\nO número {} é divísível por {} números, por isso não é um número primo!'.format(n, d))
