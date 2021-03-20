# Desafio:
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

N = int(input('Digite um número: '))

print('{:=^10}'.format(N))
print('Dobro: {}'.format(N * 2))
print('Triplo: {}'.format(N *3))
print('Raiz quadrada: {:.1f}'.format(pow(N, (1/2))))
