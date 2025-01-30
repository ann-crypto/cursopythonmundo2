from random import randint
from time import sleep

'''Crie um programa que faça o computador jogar jokenpo com voce
pedra papel e tesoura'''

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-='*11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if pc == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador GANHOU!')
    elif jogador == 2:
        print('Computador GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador GANHOU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador GANHOU!')
    else:
        print('JOGAVA INVÁLIDA!')

elif pc == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador GANHOU!')
    elif jogador == 1:
        print('Computador GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
