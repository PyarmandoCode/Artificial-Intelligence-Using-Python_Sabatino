"""
Listas

# Mutables
"""
participantes_curso =[]
participantes_curso = list() #Constructor

participantes_curso=["Juan","Pedro","Maria","Rosa","Armando"]
participantes_curso.append("Carlos") #Añade un elemento al final de la lista
participantes_curso.insert(1,"Gloria")#Añade un elemento en la posicion indicada
#print(participantes_curso[0]) #Mostrar un Elemento por su indice
participantes_curso[0]="Arturo"
participantes_curso.pop(0)
participantes_curso.remove("Armando")
size=len(participantes_curso)
#print(f"La cantidad de elementos de la lista es {size}")
#participantes_curso.sort()#Ordenar lista Asc
participantes_curso.sort(reverse=True)#Ordenar lista Desc
#print(participantes_curso)

"""
Las Tuplas son Inmutables
"""
# valores=(12,34,56) #tuple
# #valores[0]=200
# informacion_persona = ("Juan", 25, "Masculino")

# #participantes_curso=["Juan","Pedro","Maria","Rosa","Armando"]
# informacion_persona = ("Juan", 25, "Masculino") #tupla
# datos_persona=list(informacion_persona) #cast list => tuple
# datos_persona.append("DF 2034") #añadi el nuevo elemento
# informacion_persona=tuple(datos_persona) #cast tuple
# print(informacion_persona)

"""
slicing
"""