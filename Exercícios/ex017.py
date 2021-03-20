from math import hypot

CO = float(input('Qual o comprimento do cateto oposto? '))
CA = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(CO, CA)
print('A hipotenusa vai medir {:.2f}'.format(hi))
