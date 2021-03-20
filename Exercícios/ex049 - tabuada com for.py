n = int(input('Deseja ver a tabuada de qual número? '))
print()
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
