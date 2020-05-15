# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:59:52 2020

@author: patri
"""

import random

ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# defino las palabras
palabras = 'armario televisor escenario pelicula bicicleta payaso valor encerrados confinamiento herramienta coronavirus virus espacio armadura ejercito barco guerra'.split()

# función para devolver una palabra aleatoria
def buscapalabra(listapalabras):
    palabraAleatoria = random.randint(0, len(palabras) -1)
    return listapalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(ahorcado[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Aqui se reemplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    #for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        #print (letra, fin)
    print (espacio)
    print ("")

def elijeLetra(algunaLetra):
    # En esta parte se devuelve la letra que el jugador ingresó. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una letra a la vez') 
        elif letra in algunaLetra:
            print ('Ya has dicho esa letra. Prueba con una diferente')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Introduce una letra')
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print ('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscapalabra(palabras)
finJuego = False
while True:
    displayBoard(ahorcado, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuario elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(ahorcado) - 1:
            displayBoard(ahorcado, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscapalabra(palabras)
        else:
            break


