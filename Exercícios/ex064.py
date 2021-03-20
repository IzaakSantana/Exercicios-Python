n = s = t = 0

while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        t += 1
        s += n        
if t == 1:
    print('Só um número foi digitado, não há soma.')
elif t == 0:
    print("Nenhum número digitado.")
else:
    print('Foram digitados {} números e a soma entre eles é {}'.format(t, s))
