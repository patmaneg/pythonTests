# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:19:39 2020

@author: patri
"""

import random

intentosRealizados = 0
numIntentos = 10
acertado=False
print('Hola, como te llamas')
nombre = input()

numero = random.randint(1, 100)
print('Hola ' + nombre + ' vamos a empezar a jugar. Elige un número entre 1 y 100')
print('Tienes ', numIntentos, ' intentos')

while intentosRealizados < numIntentos:
    print('Dime un número:')
    adivina = input()
    try:
        adivina = int(adivina)
        
        intentosRealizados = intentosRealizados + 1
    
        if adivina < numero:
            print('El número es mayor. Te quedan ', numIntentos - intentosRealizados)
        elif adivina > numero:
            print('El número es menor. Te quedan ', numIntentos - intentosRealizados)
        else:
            print('HAS ACERTADO en ', intentosRealizados, ' intentos')
            acertado = True
            break
    except:
        print('Eso no es un número ' + nombre)
       
    

if acertado:
    print('BUEN TRABAJO')
else:
    print('El número que estaba pensando era ', numero)
    

