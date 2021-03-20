# Algoritmo pra ler um número e mostrar o dobro, triplo e a raiz quadrada.
N = int(input('Digite um número: '))
print('{:=^10}'.format(N), '\n \nDobro: {} \nTriplo: {} \nRaiz quadrada: {:.1f}'.format((N * 2), (N * 3), pow(N, (1/2))))
