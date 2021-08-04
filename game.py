from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
print('''SUAS OPÇÔES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' *12)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-='*12)
if computador == 0:
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')