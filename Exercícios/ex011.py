largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
área = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede você precisará de {}L de tinta.'.format(tinta))
