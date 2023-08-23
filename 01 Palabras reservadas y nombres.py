#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Documento principal del script.

Created on Mon Aug 22 2023
@author: Argenis Alain Gustavo Padilla Cordoba
"""

# %% Palabras reservadas en Python
# Muestra las palabras reservadas que no pueden ser usadas como identificadores en Python.
help("keywords")

# %% Operador de asignación
# Definiendo algunas variables para uso posterior.
saludo = 'Hola'
matriz = [["autobus, diesel", True], ["automivil", "gasolina", True]]
numero = 23.45

# %% Despliegue de valores en el entorno interactivo
# Mostramos el valor de las variables previamente definidas. Si intentamos acceder a una 
# variable no definida, se mostrará un error.
try:
    print(indefinido)
except NameError:
    print("La variable 'indefinido' no existe.")

# %% Asignación múltiple
# Se pueden asignar valores a múltiples variables en una sola línea.
saludo2, matriz2, numero2 = 'Hola', [["autobus, diesel", True], ["automivil", "gasolina", True]], 23.45
entero, flotante, complejo, booleano = 12, 4.5, (12.3 + 23j), True

# %% Sintaxis de nombres en Python3
# Las reglas para definir nombres de variables en Python. Se muestran algunos ejemplos.
_saludo = 'Hola'
número = 23
Numero = 45.32
יהוה = "Dios"  # Ejemplo utilizando caracteres del alfabeto hebreo.

# %% Función id()
# En Python, cada objeto tiene un ID único. Aquí mostramos cómo obtener ese ID.
saludo = "Hola"
print("ID de saludo:", id(saludo))

numeroid = 45
otro_numeroid = 45

# Ambas variables apuntan al mismo objeto, por lo que tienen el mismo ID.
print("ID de numeroid:", id(numeroid))
print("ID de otro_numeroid:", id(otro_numeroid))

# %% Asignación de múltiples nombres a un mismo objeto
# Es posible asignar diferentes nombres a un mismo objeto en memoria.
lista_1 = [1, 2, 3, 4, 5]
lista_2 = lista_1

# Ambas listas apuntan al mismo objeto, por lo que tienen el mismo ID.
print("ID de lista_1:", id(lista_1))
print("ID de lista_2:", id(lista_2))

# %% Eliminación de nombres usando del
# Es posible eliminar una variable (o nombre) usando la palabra reservada 'del'.
nombre = "Juan"
print("ID de nombre:", id(nombre))

otro_nombre = "Juan"
print("ID de otro_nombre:", id(otro_nombre))

# Se elimina la variable 'nombre' del entorno.
del nombre

# Al intentar acceder a la variable 'nombre' después de eliminarla, se genera un error.
try:
    print(nombre)
except NameError:
    print("La variable 'nombre' ha sido eliminada y ya no está disponible.")

# La variable 'otro_nombre' sigue existente.
print(otro_nombre)

# %% Contenido del espacio de nombres
# Se pueden ver todas las variables definidas en el entorno usando la función dir().
print("Variables definidas:", dir())

# Se eliminan algunas variables previamente definidas.
del saludo
del יהוה

# Se vuelve a mostrar el listado de variables después de las eliminaciones.
print("Variables después de las eliminaciones:", dir())
