velocidade = float(input('\033[36mQual a velocidade do carro?\033[m '))
if velocidade <= 80:
    print('\033[32mTudo Ok.\033[m')
else:
    multa = (velocidade - 80) * 7
    print('\033[31mVocê excedeu o limite de 80Km/h!\033[m')
    print('\033[33mVocê pagará uma multa de \033[4;33mR${:.2f}\033[m'.format(multa))
