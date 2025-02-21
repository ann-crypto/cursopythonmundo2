from random import randint

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

print('-='*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12)
print('-'*24)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu um total de: {cont}')
