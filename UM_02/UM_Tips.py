edad,nombre,altura,es_estudiante=25,"Armando",1.70,True
x= y = z = 10

frase1= "Bienvenido"
frase2="Curso de Python"

#print("Bienvenido "," Curso de python con IA "," 2024",sep="@")
#print("Bienvenido ",end="")
#print("Al Curso de Python",end="")
#print("Con Inteligencia Artifical")
#print("\t\tBienvenido al \n curso de Python")
#print("Curso de python con \"IA\" ")

"""
Tipo de Errores
-Error de Sintaxis(SyntaxError)
-Error en tiempo de Ejecuccion (Runtime errors)
-Error Semantico (Semantic Errors)
-Error Excepciones (Excepcions)

"""
try:
    division=20/0
    print(division)
except ZeroDivisionError:
    print("No se puede dividir con 0") 
except ValueError:
    print("Error Valor")
except IndexError:
    print("Error Valor")           


try:
    numero=float(input("Ingrese numero:"))
    print(numero)
except ValueError:
    print("Error Valor")    


    




      

























