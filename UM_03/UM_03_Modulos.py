"""
Caracteristicas Python
**********************
1.-Software Libre
2.-Comunidad Colaborativa (Escalable)
3.-Modulos,Bibliotecas (Repositorios)
4.-Multiplaforma (py) -Interprete
5.-Frameworks Poderosos (Django-FLASK)
   (Pandas,Numpy,Matplotplib,Seaborn,Tensorflow)
6.-Portable
7.-Interpretado
8.-Multiparadigma

Un Modulo es un archivo que contiene codigo de PYTHON incluyendo variables,funciones,clases que pueden ser reutilizados en otros programas.
"""
import math
#print(f"El Valor de pi {math.pi}")
#print(f"El valor de la raiz cuadrada de 4 {math.sqrt(4)}")
#print(f"El Coseno de pi/4 {math.cos(math.pi/4)}")
#print(f"X elevado a la potencia de Y {math.pow(2,3)}") #Calcula X Elevado de Y
#print(f"El Factorial de 5 es {math.factorial(5)}")
#print(f"El Numero de euler {math.e}")
"""
- Calcular el seno , coseno y la tangente de un angulo de radienes
math.sin(x)
math.cos(x)
math.tan(x)
- Calcular el logaritmo natural y logartimo base de 10
math.log(x)
math.log10(x)
- Convertir anguloa entre grados y radianes
math.radians(x)
math.degress(x)
"""
import statistics
datos=[2.90,10.5,14.7,23.7,10.5]
#print(f"La Media Aritmetica es {statistics.mean(datos)}")
#print(f"La Variance es {statistics.variance(datos)}") #La Variance
#print(f"La Moda de la lista de datos {statistics.mode(datos)}")
#print(f"La Desviacion estandar es {statistics.stdev(datos)} ")
"""
- mean: Calcula la media aritmética del conjunto de datos.
- median: Calcula la mediana del conjunto de datos.
- mode: Calcula la moda del conjunto de datos.
- stdev: Calcula la desviación estándar del conjunto de datos.
- variance: Calcula la varianza del conjunto de datos.
"""
import random
#Generar un numero aleatorio entre 1 10
#print(f"Numero generado es {random.randint(1,10)}")
#Generar un numero aleatorio de punto flotante entre 0 y 1
#print(f"Numero Aleatorio con punto flotante {random.random()}")
#Elegir un elemento de una lista
alumnos=["Jose","Pedro","Rosa","Manuel"]
print(f"Escojer al azar {random.choice(alumnos)}")
#Barajar una Lista Aleatoriamente
frutas=["manzana","naranja","platano","uva"]
barajado=random.sample(frutas,len(frutas))
#print(f"Lista Barajada {barajado}")
#Genera una secuencia aleatoria de 5 numeros con punto flotante
secuencia_aleatoria=[random.uniform(1,100) for _ in range(5)]
#genera un numero de punto flotante aleatorio entre a y b.
#print(f"La Secuencia aleatoria es {secuencia_aleatoria}")
#Inicializar la semilla con un valor especifico(42)
random.seed(42)
numero_aleatorio_1=random.random()
numero_aleatorio_2=random.randint(1,100)
#print(numero_aleatorio_1)
#print(numero_aleatorio_2)

import sys
#print(f"La Version de python utilizada en este curso {sys.version}")
#print(f"Obtener el Path de los modulos {sys.path}")
sys.exit("Mensaje de error y codigo de salida")









