# aluguel do carro: R$ 60 por dia. R$0.15 por km rodado.

print('=' * 50)
D = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos?' ))
T = (60 * D) + (0.15 * km)
print()
print('=' * 50)
print('R$60 por dia e R$0.15 por km.')
print('Dias alugaos: {}\nKm percorridos: {}\nTotal a pagar: R${:.2f}'.format(D, km, T))
print('=' * 50)
