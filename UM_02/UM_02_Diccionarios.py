"""
Diccionarios
-Almacenar datos en formato clave-valor
(Key - Value)
Estructura de datos
"""
mi_diccionario = {}
mi_diccionario = dict()

mi_diccionario = {
    "nombre":"Juan","edad":30,"ciudad":"california"
}

print(mi_diccionario["ciudad"])
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])

mi_diccionario["sexo"]="M"
mi_diccionario["ciudad"]="Washington"
del mi_diccionario["sexo"]

#Buscar una valor por su clave , si no el encuentra el valor me devuelve el
#Mensaje Predeterminado
valor = mi_diccionario.get("nombre","No Existe el valor")

print(f"El valor del diccionario es {valor}")

#for k ,v in mi_diccionario.items():
#    print(f"La Clave {k} y los valores {v}")

# print(mi_diccionario.keys())
# print(mi_diccionario.values())

usuarios = [
        {"nombre":"Juan","edad":30,"ciudad":"california"},
        {"nombre":"Pedro","edad":20,"ciudad":"Las Vegas"},
        {"nombre":"Manuel","edad":35,"ciudad":"california"},
        {"nombre":"Gustavo","edad":22,"ciudad":"california"},
        {"nombre":"Percy","edad":19,"ciudad":"Miami"},
        {"nombre":"Andrea","edad":31,"ciudad":"california"}
]
size=len(usuarios)
#print(f"La Cantidad de registros de mi Lista {size}")
#print(usuarios[4]['nombre'])

def buscar_usuario_nombre(nom):
    try:
        #nombre_bus=input("Ingrese Nombre a Buscar:")
        for data in usuarios:
            if nom in data['nombre']:
                print(f"Usuario encontrado {data}" )
                break
        else:
            print("Usuario no ubicado")
    except Exception as err:
        print("Ocurrio un error consulte la web en 24 horas")        

    




