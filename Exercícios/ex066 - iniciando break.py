soma = total = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    soma += n
    total += 1
if total == 1:
    print('\nSó um valor foi digitado, não há soma.')
elif total == 0:
    print('\nNenhum valor foi digitado.')
else:
    print(f'\nA soma dos {total} valores foi {soma}!')
