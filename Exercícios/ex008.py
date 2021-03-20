# Desafio:
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

M = float(input('Digite uma distância em metros: '))
cm = M * 100
mm = M * 1000
km = M / 1000
print('A medida de {}m corresponde a {}km, {:.0f}cm e {:.0f}mm'.format(M, km, cm, mm))
