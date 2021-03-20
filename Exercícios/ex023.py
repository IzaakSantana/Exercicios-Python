N = int((input('Digite um número entre 0 e 9999: ')))
U = N // 1 % 10
D = N // 10 % 10
C = N // 100 % 10
M = N // 1000 % 10
print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(U, D, C, M))
