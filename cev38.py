'''Escreva um programa que leia dois números inteiros e compare-os, monstrando na tela uma mensagem
o primeiro valor é maior
o segundo valor é maior
nao existe valor maior, os dois são iguais.
exemplo: 3 e 5 o 5 é o segundo valor e é o maior. etc'''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são iguais.')
