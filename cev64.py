'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999. que é a condição de parada.
no final, mostre quantos números foram digitados e qual foi a soma entre eles
(Desconsiderando o flag, ou seja, esse 999 de parada).'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
