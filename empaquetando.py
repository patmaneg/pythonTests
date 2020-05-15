# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:40:22 2020

@author: patri
"""

## probando a crear funciones en otro directorio y ser llamadas desde python
## con el fichero __init__.py

# He creado dos funciones en el directorio funciones,
# y un __init__.py - primero vacío

import funciones

funciones.imprimir_texto("texto")
funciones.func_mayor(1, 2)
