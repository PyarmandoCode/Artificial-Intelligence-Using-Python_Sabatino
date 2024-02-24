"""
Crear un programa que ingrese 3 notas de un alumnos y calcule su promedio
general y me indique si el alumno aprobo o no el curso
"""

# suma=0
# con =0
# for nota in range(3):
#     notas = float(input(f"Ingrese Nota {nota}:"))
#     suma +=notas #acumulando notas
#     con +=1 #contando notas
# promedio = suma / con    
# if promedio>=10.5:
#     print("El Alumno aprobo el curso")
# else:
#     print("El Alumno Desaprobo el curso")   

def calcular_notas():
    try:
        lista_notas=list()
        for nota in range(3):
            notas = float(input(f"Ingrese Nota {nota}:"))
            lista_notas.append(notas)
        suma_notas=sum(lista_notas)
        promedio = suma_notas / 3
        mensaje = "Aprobo el curso" if promedio >=10.5 else "No Aprobo el curso"
        return mensaje
    except Exception as err:
        print(f"Ocurrio un error en el codigo {err}")    
    else:
        print("Todo correctamente")    
        pass
    finally:
        print("Cerrando todos los Objetos")
        pass

calcular_notas()
