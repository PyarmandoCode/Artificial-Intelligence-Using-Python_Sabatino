# edad_persona=int(input("Ingrese la edad:"))
# if edad_persona>=18:
#     #bloque True
#     print("La Persona es mayor de edad")
    
# else:
#     #bloque False
#     print("La Persona es menor de edad")   

"""
AREA
====
[S]istemas=2%
[M]arketing=3%
[C]ontabilidad=4%
0
""" 
# area=input("Ingrese el Area en que labora:")
# if area.lower()=="s":
#     bon=0.02
# elif area.lower() =="m":
#     bon=0.03
# elif area.lower() =="c":
#     bon = 0.04
# else:
#     bon=0        
# print(f"La Bonificacion Obtenida es {bon}")
  

# frase="El Gran Elefante Blanco"
# print(frase.lower())

# nota=float(input("Ingrese la Nota Obtenida:"))
# if nota >=10.5:
#     print("El Alumno Aprobo el Curso")
# else:
#     susti=float(input("Ingrese el Sustitutorio:"))    
#     prome = (susti+nota) /2
#     if prome>=10.5:
#         print("El Alumno Aprobo el curso en el sustitutorio")
#     else:
#         print(f"El Alumno debe llevar el curso nuevamente {prome}")    

"""
Producto Calcular el descuento hacia un producto
=================================================
0 - 5 = 0
6 - 20 = 0.02
21 - 50 =0.03
>50 0.05
"""
precio=float(input("Ingrese el Precio del producto:"))
if 0 <= precio <=5:
    desc=0
elif 6 <= precio <=20:
    desc=0.02
elif 21 <= precio <=50:
    desc=0.03
else:
    desc=0.05
print(f"El Descuento obntenido es {desc} ")    









