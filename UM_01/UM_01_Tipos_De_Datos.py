"""
Trabajando con fechas
=====================
from datetime import datetime
fecha_actual=datetime.now()
print(fecha_actual)
"""

"""
Tipos de datos en Python (Primitivos)
1.-Numerico
 - int
 - float
2.-Cadenas
 - str
3.-Logicos
 - bool
4.-Estructura de Datos
 -Listas
 -Tuplas
 -Diccionarios
 -Conjuntos (set)   
"""

"""
PEP8='PROPUESTA DE MEJORA EN PYTHON'
"""

#SNAKE_CASE
#Malo
    #x=5
    #y="hola"

nombre_curso = 'Python' #str
precio_curso = 1200.90 #float
horas_curso = 66 #int
estado_curso = True #bool
participantes =["Victor","Yair","Luis","Armando"]#list

#print(type(nombre_curso))
#print(type(str(precio_curso))) #float
#print(type(int(estado_curso))) #bool
#print(int(precio_curso))
"""
CONVERSION D DATOS (cast)

- int
- str
- float
- bool

"""
"""
FORMATO DE CADENA
"""
nombre_curso = 'Python' #str
profesor_curso="Armando" #str
precio_curso = 1200.98999 #float
horas_curso = 66 #int
estado_curso = True #bool
participantes =["Victor","Yair","Luis","Armando"]#list

cadena= nombre_curso + profesor_curso
total = precio_curso + horas_curso
cadena2=nombre_curso + str(precio_curso) #Tradional
cadena3=f"Este es el Nombre del curso {nombre_curso} y su precio {round(precio_curso,1)} y su profesor es {profesor_curso} y el primer alumno matriculado es {participantes[0]}" #Pythonico

print(cadena3)