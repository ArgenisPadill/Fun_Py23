#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Aug 22 2023
@author: Argenis Alain Gustavo Padilla Cordoba
"""

# %% Expresiones
"""
Las expresiones son combinaciones válidas en Python que retornan un valor. Pueden estar compuestas por 
variables, valores literales, operadores y llamadas a funciones.
"""

# Asigna el valor 78.3 a la variable "numero".
numero = 78.3

# Muestra el valor de "numero".
numero

# Suma de dos números.
1 + 1

# Evalúa si 45 es mayor o igual a 11.
45 >= 11

# Convierte el texto "carro" a mayúsculas usando el método upper().
"carro".upper()

# Obtiene y muestra la longitud del texto "Saludo".
len('Saludo')

# %% Ejecución de varias expresiones en una sola línea
"""
Python permite ejecutar múltiples expresiones en una línea si se separan por un punto y coma (;). 
No obstante, sólo se muestra el resultado de la última expresión.
"""

# Asigna, convierte y suma: sólo se mostrará el resultado de a + 5.
a = 3; "hola".upper(); a + 5

# Comprueba el valor actual de "a".
a

# Suma, repite y compara: ninguno se muestra porque la última expresión finaliza con un punto y coma.
a += 11; "amigos" * 3; a == 1;
a

# %% Expresiones en el entorno interactivo
"""
Cuando trabajamos en un entorno interactivo (como el intérprete de Python o IPython), 
cada expresión se evalúa y muestra inmediatamente.
"""

# Multiplicación.
4 * 3

# Comparación.
15 == 25

# Concatenación de cadenas.
'hola' + ' mundo'

# %% Comentarios en Python
"""
Los comentarios son fragmentos de texto que el intérprete de Python ignora. 
Se usan para explicar o anotar el código, facilitando su comprensión.
"""

# Comentario de una sola línea precedido por #.
15 + 23  # Comentario después de una expresión. Resultado: 38.

# %% Docstrings en Python
"""
Los docstrings son comentarios de varias líneas encerrados entre triples comillas dobles (""") """
o triples apóstrofes ('''). Se usan principalmente para documentar módulos, funciones y clases.
"""

def funcion():
    """
    Función de ejemplo que muestra el uso de un docstring.
    Los docstrings al principio de una función sirven para documentar su propósito y uso.
    """
    print("Hola")
    # Los docstrings también pueden ir en medio del código, aunque no es la práctica común.
    """Este docstring no forma parte de la documentación de la función."""
    
# Muestra la documentación de la función usando "help()".
help(funcion)
