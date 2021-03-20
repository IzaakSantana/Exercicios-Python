while True:
    print('-' * 36)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 36)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
print('Programa encerrado!')
