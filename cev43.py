'''Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
acima de 40:
obesidade mórbida'''

print('-*-' * 6)
print('CALCULADORA DE IMC')
print('-*-' * 6)

peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc > 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc > 25 and imc < 30:
    print('Você está em SOBREPESO.')
elif imc > 30 and imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
