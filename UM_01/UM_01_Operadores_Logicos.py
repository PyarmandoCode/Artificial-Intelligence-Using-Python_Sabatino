"""
Operadores de comparación:
Igualdad: ==
Desigualdad: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=

and: Devuelve True si ambas expresiones son verdaderas.
or: Devuelve True si al menos una de las expresiones es verdadera.
not: Niega la expresión booleana; devuelve False si la expresión es verdadera y viceversa. (Negacion Unaria)

"""
edad=18
licencia_conducir=True

manejar= not edad>=18 and licencia_conducir==True

print(manejar)
