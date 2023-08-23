#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 2023

@author: Argenis Alain Gustavo Padilla Cordoba
"""

#%%Palabras reservadas dentro de Python
help("keywords")


#%%Operador de asignacion 

saludo ='Hola'

matriz= [["autobus, diesel", True],["automivil","gasolina",True]]

numero = 23.45


#%% Despliege de valores ligados a un nombre en el entorno interactivo

#cada ima de las instrucciones regresara el objeto que corresponde a cada nombre asignado.


saludo

matriz

numero

# si se llama a trar un objeto que no existe en el universo de nombres o variables  nostrara un tipo de NameError

indefinido


#%% asiganacion de multiples nombres  a igual numero de objetos

saludo2, matriz2, numero2 = 'Hola', [["autobus, diesel", True],["automivil","gasolina",True]], 23.45

entero, flotante, complejo,booleano = 12 , 4.5, (12.3+23j) , True


#%% Sintaxis para alaboracion de nombres en Python3

""" 
*Python 3 acepta el uso de Unicode, por lo que es posible utilizar cualquier caracter alfabético, 
incluso aquellos que no pertencen al alfabeto occidental para la elaboración de nombres.

*Los nombres pueden empezar con un guión bajo _ o un caracter alfabético.

*Después del primer caracter, se pueden utilizar caracteres alfabéticos, números y/o guiones bajos.

*No se permiten caracteres distintos a los alfabéticos o que pudieran confundirse con operadores como |, ~, #, -, etc.

*Se pueden utilizar mayúsculas, pero cabe señalar que Python es sensible a mayúsculas.

"""

_saludo = 'Hola'
número = 23
Numero = 45.32

"""Ejemplo el usos de caracteres de alfabetos distintos a los occidentales utilizando el alfabeto hebreo,
 el cual se escribe de derecha a izquierda."""


יהוה ="Dios"

#%% La función id().
"""
Cada objeto cuenta con un número identificador, el cual corresponde a la posición en la que se encuentra almacenado en la memoria.

La función id() permite acceder al número identificador de cada objeto usando su nombre como argumento.

La sintaxis es la siguiente:
"""
saludo = "Hola"

id(saludo)

"""
Asignación de múltiples nombres al mismo objeto.
Python es un lenguaje que gestiona de forma automática el uso de la memoria y trata de optimizar su uso, por lo que en caso 
de que se defina un objeto idéntico a otro ya existente, no creará uno nuevo, sino que ligará el nuevo nombre al objeto existente.
"""

#En la siguientes celdas se le asignarán dos nombres al objeto con valor igual a 45.

numeroid = 45
otro_numeroid = 45


#Aún cuando se definen de forma separada, el resultado de la función id() es el mismo para cada nombre.

id(numeroid)
id(otro_numeroid)

#%%Asignación de múltiples nombres a un objeto.
"Para asignarle más de un nombre al mismo objeto, sólo es necesario referenciar un nombre existente al nuevo nombre."

#Las siguientes celdas le asignarán el nombre lista_1 y lista_2 al mismo objeto.

lista_1 = [1, 2, 3, 4, 5]
lista_2 = lista_1
#Se puede observar que el número identificador corresponde al mismo objeto, aún cuando tiene otro nombre.

id(lista_1)
id(lista_2)

#%%Eliminación de nombres mediante la declaración del.
"""
La declaración del funciona de la siguiente manera:
 * Desliga al nombre de un objeto en el espacio de nombres.
 * Elimina al nombre del espacio de nombres.
 * En caso de que el objeto no esté ligado a otro nombre en el espacio de nombres, el intérprete de Python podría desecharlo de forma automática.
 * El modo en el que un objeto puede ser destruido varía dependiendo del tipo de objeto.
"""

#Se creará el objeto "Juan" al cual se le asignarán los nombres nombre y otro_nombre.

nombre = "Juan"

id(nombre)

otro_nombre = "Juan"

id(otro_nombre)

#Se eliminará nombre del espacio de nombres.

del nombre

#Debido a que nombre fue eliminado del espacio de nombres, la siguiente celda regresará un erro de tipo NameError.

nombre

#El objeto "Juan" sigue existiendo en la memoria, debido a que aún existe un nombre al que está ligado.

otro_nombre

#%%Despliegue del contendio del espacio de nombres.
"La función dir() regresa el listado de nombres del espacio de nombres principal."

#Se puede apreciar que el listado incluye una serie de nombre especiales 
#y todos los nombres que se han definido a lo largo de este scrip

dir()

#La siguiente celda elimina el nombre saludo, el cual fue definido previamente.

del saludo


#El resultado es que el nombre saludo ya no será enlistado al ejecutar la función dir().
dir()


#Lo mismo sucede al eliminar el nombre יהוה.
del יהוה

dir(otro_nombre)



