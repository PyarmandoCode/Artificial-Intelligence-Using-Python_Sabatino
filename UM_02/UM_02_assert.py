"""
assert .- Es una palabra clave reservada para realizar afirmaciones o comprobaciones de condiciones

Sintaxis:
assert expresion , mensaje_de_error
"""
try:
    edad = int(input("Ingrese la edad:"))
    assert edad>0 , "Error: La edad no puede ser negativa"
    print(f"edad ingresada correcta {edad}")
except (ValueError,AssertionError) as e:
    print(f"Error Producido {e}")   


#import keyword #Modulo
#print(keyword.kwlist)

