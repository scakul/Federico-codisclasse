import matplotlib.pyplot as plt
from graphic import grafica
from random import randint
from time import sleep

def distancia():
    persones = randint(0,1)
    return persones

llistapersones = []
minuts = 0
while minuts < 10:
    persones = 0
    contador = 0 
    for segons in range(60):
        pasa = distancia()
        if pasa >= 1:
            contador = contador + 1
        print(contador)    
        sleep(1)
    llistapersones.append(contador)
    minuts += 1
    print(llistapersones)
grafica(llistapersones)
