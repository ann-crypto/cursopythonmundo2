from time import sleep
import emoji

'''Faça um programa que monstre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

for count in range(10, -1, -1):
    print(count)
    sleep(0.5)
print(emoji.emojize('💥💥 BUM! BUM! POOOW! 💥:collision:', language='alias'))
