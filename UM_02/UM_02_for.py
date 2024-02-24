"""
Bucle For

-Se debe utilizar cuando conocemos las veces que el bucle va iterar

Sintaxis:

for <var> in range(v1,vf,step):
     <cuerpo del bucle>
else:
     <nada que iterar>     
<fin bucle>

"""
#for vuelta in range(5,10,2):
#    print(f"{vuelta} Bienvenido al Curso de Python con IA")
#print("Fin del bucle")    


"""
Imprimir una lista con numeros Pares (1,10)

lista_pares=list()#Constructor
lista_impares=list()

for vuelta in range(1,11):
    if vuelta % 2 == 0:
        lista_pares.append(vuelta)
    else:
        lista_impares.append(vuelta)    
print(f"Lista de Pares {lista_pares}")
print(f"Lista de ImPares {lista_impares}")
"""

"""
Crear un Programa que recorra la lista y cuando encuentre
un numero impar debe terminar el reccorido del bucle
Break.-Termina la ejecucion del Bucle

numeros =[2,4,1,6,8,9,10]
for vuelta in numeros:
    if vuelta % 2 !=0:
        print(f"El Primer Numero impar que encontro fue {vuelta}")
        break #Interrumpir la ejecucion del bucle
        

numeros =[1,2,3,4,5,6,7,8,9,10]
for vuelta in numeros:
    if vuelta % 2 !=0:
        continue #Salta el valor actual del bucle
    print(vuelta)        

"""

"""
#si encuentra el numero  imprimir un mensaje indicando que se interrumpio el bucle

#si el bucle completa la iteracion sin interrupciones se imprime un mensaje
indicando que el bucle ha recorrido todos los numeros sin interrupciones
"""
numeros = [1,2,3,0,5]
for numero in numeros:
    if numero ==0:
        print("El Numero es cero, El Bucle se Interrumpe")
        break
    print(f"Procesando el numero {numero}")
else:
    print("El Bucle ha reccorido todos los numeros sin interrupciones")




















    
        




    