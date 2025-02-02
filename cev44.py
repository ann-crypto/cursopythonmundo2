'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
a vista dinheiro/cheque: 10% de desconto
a vista no cartao: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartao: 20% de juros.'''

print('{:=^40}'.format(' LOJAS SIQUEIRA '))
preço = float(input('Preço das compra: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparcelas = int(input('Quantas parcelas? '))
    parcela = total / totparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparcelas, parcela))
else:
    total = preço
    print('\033[31mOPÇÃO INVALIDA DE PAGAMENTO! Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
