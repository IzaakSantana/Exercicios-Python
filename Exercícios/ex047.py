print('Números pares entre 1 e 50')
print()
totpar = 0
for intervalo in range(2, 51, 2):
    totpar += 1
    print(intervalo)
print()
print('Houve um total de {} números pares.'.format(totpar))
