"""
Esta es una pruba de como funcionan los "if statements".
"""
__author__ = "Cesarcd"
__credit__ = ["Cesarcd", "BigXKu (FBB)"]

# Inputs
name = input("¿Cómo te llamas? ") # Obtener nombre
gender = input("¿Cuál es tu sexo (M o H)? ") # Obtener sexo

# Condicionales:
if gender == "M": # Mujer
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"

# Resultado
print("Tu grupo es " + group)