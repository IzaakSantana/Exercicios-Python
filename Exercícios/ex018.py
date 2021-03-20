import math

an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo {} tem o seno de {:.2f}'.format(an, seno))
print('O ângulo {} tem o cosseno de {:.2f}'.format(an, cos))
print('O ângulo {} tem o tangente de {:.2f}'.format(an, tan))
