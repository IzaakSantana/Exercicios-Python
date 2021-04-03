# Desafio 
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []

print("=" * 20)
print("MEGA SENA")
print("=" * 20)

jogos = int(input("Quantos jogos você quer sortear? "))

