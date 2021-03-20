# encoding=utf-8
from playsound import playsound
import prompt

# Código antigo...... logo ele está muito mal feito, mal programado e etc. Tenho vergonha disso.
# Porém! Fiz uma versão melhorada dele, que inclusive tem como adicionar novas músicas.

arquivo = ''
nome = ''
esc = 0

while esc != 1:
    print('=' * 5)
    print('Menu:')
    print('=' * 5)
    print('=' * 40)
    print('''
    [1] Lovely - Bilie Eilish
    [2] Te vi na rua ontem - Konai
    [3] Deixa - Lagum 
    [4] Libra - A banca 021
    [5] Heathens - Twenty One Pilots
    [6] Believer - Imagine Dragons
    [7] Rap Lord - Haikaiss
    [8] Rap God - Eminem
    [9] - Tocar todas -
    ''')  # menu
    print('=' * 40)
    m = 0
    while m == 0 or m > 9:
        m = int(input('Digite o número da música escolhida. '))
        if m == 1:
            arquivo = 'musicas/lovely.mp3'
            nome = 'Lovely - Billie Eilish'
        elif m == 2:
            arquivo = 'musicas/tevinaruaontem.mp3'
            nome = 'Te vi na rua ontem - Konai'
        elif m == 3:
            arquivo = 'musicas/deixa.mp3'
            nome = 'Deixa - Lagum'
        elif m == 4:
            arquivo = 'musicas/libra.mp3'
            nome = 'Libra - A banca 021'
        elif m == 5:
            arquivo = 'musicas/heathens.mp3'
            nome = 'Heathens - Twenty One Pilots'
        elif m == 6:
            arquivo = 'musicas/believer.mp3'
            nome = 'Believer - Imagine Dragons'
        elif m == 7:
            arquivo = 'musicas/rap lord.mp3'
            nome = 'Rap Lord - Haikaiss'
        elif m == 8:
            arquivo = 'musicas/rap god.mp3'
            nome = 'Rap God - Eminem'
        elif m == 9:
            nome = 'Lovely - Billie Eilish'
            print(f'Tocando agora: {nome}')
            playsound('musicas/lovely.mp3')
            prompt.cls()
            nome = 'Te vi na rua ontem - Konai'
            print(f'Tocando agora: {nome}')
            playsound('musicas/tevinaruaontem.mp3')
            prompt.cls()
            nome = 'Deixa - Lagum'
            print(f'Tocando agora: {nome}')
            playsound('musicas/deixa.mp3')
            prompt.cls()
            nome = 'Libra - A banca 021'
            print(f'Tocando agora: {nome}')
            playsound('musicas/libra.mp3')
            prompt.cls()
            nome = 'Heathens - Twenty One Pilots'
            print(f'Tocando agora: {nome}')
            playsound('musicas/heathens.mp3')
            prompt.cls()
            nome = 'Believer - Imagine Dragons'
            print(f'Tocando agora: {nome}')
            playsound('musicas/believer.mp3')
            prompt.cls()
            nome = 'Rap Lord - Haikaiss'
            print(f'Tocando agora: {nome}')
            playsound('musicas/rap lord.mp3')
            prompt.cls()
            nome = 'Rap God - Eminem'
            print(f'Tocando agora: {nome}')
            playsound('musicas/rap god.mp3')
        else:
            print('Opção inválida!')

    print('=' * 37)
    print(f'Tocando agora: {nome}')
    print('=' * 37)

    playsound(arquivo)
    esc = int(input('''
    [1] Sair
    [2] Tocar outra música
    '''))
    prompt.cls()
