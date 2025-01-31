'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for impar, desconsiderá-lo'''
soma = 0
cont = 0
for count in range(1,7):
    num = int(input('Digite o {} número: '.format(count)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} números PARES e a soma foi {}.".format(cont, soma))
