# Algoritmo pra ler um número e mostrar o dobro, triplo e a raiz quadrada.
N = int(input('Digite um número: '))

print('{:=^10}'.format(N))
print('Dobro: {}'.format(N * 2))
print('Triplo: {}'.format(N *3))
print('Raiz quadrada: {:.1f}'.format(pow(N, (1/2))))
