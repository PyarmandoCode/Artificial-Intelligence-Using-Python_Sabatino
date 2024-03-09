"""
Creear un Programa para automatizar la planilla de sueldos de una empresa
con las siguientes caracteristicas:
1.-Se debe tener algunos empleados ya registrados en diccionarios (3)
2.-Se debe tener la posibilidad de poder ingresar nuevos empleados
3.-Se debe calcular la suma de sueldos y se debe obtener el promedio de ese
mes
4.-Utilizar excepciones y funciones
5.-posibilidad de visualizarlo
"""
trabajadores = [
    {"codigo":"Trab_01","ht":40},#0
    {"codigo":"Trab_02","ht":46},#1
    {"codigo":"Trab_03","ht":50},#2
]
pago_hora=20

def registro_empleado(codpar,htpar):
    try:
        nuevo_empleado = {
            "codigo":codpar,
            "ht":htpar
        }
        trabajadores.append(nuevo_empleado)
    except Exception as err:
        return f"Ocurrio una error {err}"
    else:
        return "Empleado Agregado con exito!!"
    
def listar_empleados():
    try:
        global pago_hora
        sum_horas=0
        for index,empleado in enumerate(trabajadores):
            total_pago=trabajadores[index]["ht"]*pago_hora
            sum_horas += total_pago
        return f"La suma total de la planilla es {sum_horas} y el promedio {sum_horas/len(trabajadores)}"
    except Exception as err: 
        return f"Ocurrio un error {err}"
    
while True:
    codigo=input("Ingrese el Codigo:")
    ht=int(input("Ingrese las HT:"))
    registro_empleado(codigo,ht)
    resp=input("¿Desea Continuar:")
    if resp == "n":
        break
print(listar_empleados())






