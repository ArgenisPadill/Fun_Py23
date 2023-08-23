#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
##################################################
Created on Wed Aug 23 2023              
@author: Argenis Alain Gustavo Padilla Cordoba 
##################################################
"""
#%% Tipos de datos.

"""
Python ha evolucionado para ofrecer poderosos tipos de datos que lo diferencian 
de otros lenguajes de programación por su sencillez y flexibilidad.
"""

# Tipos dinámicos.
"""
Python es un lenguaje que no requiere definir el tipo de un objeto. 
El intérprete "infiere" el tipo de dato.
"""
# Fuertemente tipado.
"""Existen operaciones que no están permitidas entre tipos incompatibles."""


# Los tipos son clases.
"""
En Python, todos los elementos son objetos. Los datos, una vez identificados, 
se convierten en objetos instanciados del tipo al que pertenecen.
"""



# Tabla de tipos de datos en Python
"""
Tipo de dato   | Colección | Indexable | Mutable | Contenido                       | Ejemplo
---------------|-----------|-----------|---------|---------------------------------|-------------------------
int            | NO        | NO        | NO      | Números enteros                 | -12
float          | NO        | NO        | NO      | Números de punto flotante       | 4.361
complex        | NO        | NO        | NO      | Números complejos               | (41.6-11.3j)
bool           | NO        | NO        | NO      | Valores booleanos               | True
NoneType       | NO        | NO        | NO      | Sin valor                       | None
str            | SÍ        | Numérico  | NO      | Caracteres Unicode              | 'Gödel'
bytes          | SÍ        | Numérico  | NO      | Caracteres ASCII                | b'Hola'
bytearray      | SÍ        | Numérico  | SÍ      | Caracteres ASCII                | bytearray(b'Hola')
list           | SÍ        | Numérico  | SÍ      | Cualquier objeto                | [1, 2.0, 'Tres']
tuple          | SÍ        | Numérico  | NO      | Cualquier objeto                | (1, 2.0, 'Tres')
dict           | SÍ        | Por clave | SÍ      | Pares clave:valor               | {'nombre':'Juan', 'promedio':10}
set            | SÍ        | NO        | SÍ      | Objetos inmutables              | {1, False, 'María'}
frozenset      | SÍ        | NO        | NO      | Objetos inmutables              | frozenset({1, False, 'María'})
"""




#%% int: Números enteros.
"""
Qué es: Representa números enteros, sin punto decimal.
Utilidad: Fundamental para representar conteos, índices o cualquier cantidad que no requiera fracciones. 
Por ejemplo, el número de usuarios registrados en un sitio web.
"""

# Ejemplo: Declarar un número entero y mostrarlo.
numero_entero = -12
print(numero_entero)

#%% float: Números de punto flotante.
"""
Qué es: Representa números reales con punto decimal.
Utilidad: Ideal para representar medidas que requieren precisión, 
Por ejemplo, el peso de un objeto, la altura de una persona o el saldo bancario.
"""

# Ejemplo: Declarar un número de punto flotante y mostrarlo.
numero_flotante = 4.361
print(numero_flotante)

#%% complex: Números complejos.
"""
Qué es: Números con una parte real y otra imaginaria.
Utilidad: Específicos para áreas como la ingeniería eléctrica o la matemática avanzada.
Por ejemplo, análisis de circuitos eléctricos.
"""

# Ejemplo: Declarar un número complejo y mostrarlo.
numero_complejo = (41.6-11.3j)
print(numero_complejo)

#%% bool: Valores booleanos (True o False).
"""
Qué es: Solo puede tener dos valores: True o False.
Utilidad: Perfecto para representar estados binarios, 
Por ejemplo,como un interruptor que puede estar encendido o apagado.
"""
# Ejemplo: Declarar un valor booleano y mostrarlo.
valor_booleano = True
print(valor_booleano)

#%% NoneType: Representa la ausencia de valor.
"""
Qué es: Solo tiene un valor posible: None.
Utilidad: Útil para indicar que algo está vacío o sin definir. 
Por ejemplo, un valor por defecto de un argumento en una función.
"""
# Ejemplo: Declarar una variable sin valor y mostrarla.
sin_valor = None
print(sin_valor)

#%% str: Caracteres Unicode.
"""
Qué es: Cadena de texto que puede contener cualquier carácter Unicode.
Utilidad: Esencial para representar palabras, frases, nombres, mensajes, y más. 
Por ejemplo, el nombre de una persona o la descripción de un producto.
"""
# Ejemplo: Declarar una cadena de caracteres Unicode y mostrarla.
cadena_unicode = 'Gödel'
print(cadena_unicode)

#%% bytes: Caracteres ASCII.
"""
Qué es: Secuencia inmutable de bytes.
Utilidad: Usado para trabajar con datos a nivel binario. Esencial para procesar archivos como imágenes o audio en formato raw.
"""
# Ejemplo: Declarar una cadena de caracteres en ASCII y mostrarla.
cadena_ascii = b'Hola'
print(cadena_ascii)

#%% bytearray: Similar a bytes, pero mutable.
"""
Qué es: Similar a bytes, pero su contenido puede ser modificado.
Utilidad: Útil cuando necesitas trabajar con datos binarios y cambiarlos en el proceso, 
por ejemplo, modificar una imagen antes de guardarla.
"""
# Ejemplo: Declarar un bytearray y mostrarlo.
byte_array = bytearray(b'Hola')
print(byte_array)

#%% list: Colección de objetos en una lista.
"""
Qué es: Colección ordenada de objetos que pueden ser de cualquier tipo.
Utilidad: Versátil para almacenar colecciones de elementos, desde una lista de números hasta una lista de objetos complejos.
"""

# Ejemplo: Declarar una lista con diferentes tipos de datos y mostrarla.
lista_variada = [1, 2.0, 'Tres']
print(lista_variada)

#%% tuple: Colección inmutable de objetos en una tupla.
"""
Qué es: Similar a la lista, pero una vez creada no puede ser modificada.
Utilidad: Ideal para representar datos que no deberían cambiar, como las coordenadas de un punto en el espacio.
"""

# Ejemplo: Declarar una tupla con diferentes tipos de datos y mostrarla.
tupla_variada = (1, 2.0, 'Tres')
print(tupla_variada)

#%% dict: Colección de pares clave:valor.
"""
Qué es: Colección de pares clave-valor.
Utilidad: Perfecto para representar datos estructurados, como un contacto con "nombre" y "teléfono" o configuraciones de un programa.
"""
# Ejemplo: Declarar un diccionario y mostrarlo.
diccionario = {'nombre':'Juan', 'promedio':10}
print(diccionario)

#%% set: Colección de objetos inmutables, sin duplicados.
"""
Qué es: Colección sin orden, sin duplicados y sus elementos son inmutables.
Utilidad: Muy útil para operaciones de conjunto, como determinar la intersección entre dos conjuntos,
 o simplemente asegurarse de que no haya duplicados.
"""
# Ejemplo: Declarar un conjunto y mostrarlo.
conjunto = {1, False, 'María'}
print(conjunto)

#%% frozenset: Similar a set, pero inmutable.
"""
Qué es: Igual que el set, pero no puede ser modificado después de su creación.
Utilidad: Ideal para cuando se necesita un conjunto que no se modifique, garantizando la integridad de los datos.
"""
# Ejemplo: Declarar un frozenset y mostrarlo.
conjunto_inmutable = frozenset({1, False, 'María'})
print(conjunto_inmutable)