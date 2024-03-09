"""
sets(conjuntos)
-Es una coleccion no ordenada de elementos unicos 
-Manejan funciones o metodos para sus operaciones
"""

conjunto_vacio = set()
conjunto_vacio={8,2,5,6}
conjunto_vacio.add(1)
conjunto_vacio.add(2)
conjunto_vacio.remove(8)
#print(conjunto_vacio)

conjunto3={1,2,3,4,5}
conjunto4={3,4,5,6,7}

union_conjuntos=conjunto3.union(conjunto4)

interseccion_conjuntos=conjunto3.intersection(conjunto4)
diferencia_conjuntos=conjunto3.difference(conjunto4)
#print(diferencia_conjuntos)

lista_con_duplicados=[1,2,2,3,4,4,5,6,6]

conjunto_sin_duplicados=set(lista_con_duplicados)
print(conjunto_sin_duplicados)
