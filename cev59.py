from time import sleep
'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
seu programa deverá realizar a operação solicitada em cada caso.'''

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>> Qual é a sua opção? '''))
    if escolha == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}.'.format(valor1, valor2, soma))
    elif escolha == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} e {} é {}.'.format(valor1, valor2, mult))
    elif escolha == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é {}.'.format(valor1, valor2, maior))
    elif escolha == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=' * 13)
    sleep(1)
print('Fim do programa!')
