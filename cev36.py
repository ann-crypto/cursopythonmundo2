'''Escreva um programa para parovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
Considerações: casa de 200 mil reais, meu salario é de 1 mil reais, e eu quero pagar em 50 anos.
todo mes eu pago uma parcela, sem correr juros, etc. verificar o valor da prestacao de tantos por mes
por 50 anos e se vai poder ou nao a casa, porque nao vai poder exceder 30% do salario'''

casa = float(input('Valor da casa? R$ '))
salario = float(input('Salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
