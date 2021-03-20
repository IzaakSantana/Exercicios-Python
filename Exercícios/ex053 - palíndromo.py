# desisto

frase = str(input('Digite uma frase: ')).strip().upper().split()
frasej = ''.join(frase)  # junta a frase separada
fraseL = []  # lista vazia
fraseL2 = []  # lista vazia
c2 = 0  # Conta o final da frase.

for c in range(0, len(frasej)):  # A lista fraseL recebe um por um os caracteres de frase
    fraseL += frasej[c]

for c in range(0, len(frasej)):  # A lista L2 recebe um por um, só que ao contrário os caracteres de fraseL
    if c == 0:
        c2 = 1
    else:
        c2 += 1
    fraseL2 += fraseL[len(fraseL) - c2]

if fraseL == fraseL2:  # Verifica se é palíndromo.
    print('{} ao contrário fica {}, por isso é um palíndromo!'.format(''.join(fraseL), ''.join(fraseL2)))
else:
    print('{} ao contrário fica {}, por isso não é um palíndromo.'.format(''.join(fraseL), ''.join(fraseL2)))
