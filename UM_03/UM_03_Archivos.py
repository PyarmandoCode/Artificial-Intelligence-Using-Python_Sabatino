"""
Aperturar el archivo CSV 
Y trabajar solo con los precios mayores o igual 140
import csv
con=0
listavalores=list()
with open('./UM_03/archivos/productos_marzo_2024.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        if con>=1:
            if int(row[2]) >=140:
                listavalores.append([row[0],row[1],int(row[2])])
        con +=1

for indixe,valor in enumerate(listavalores):
    print(f"{indixe} {valor}")

"""
import csv
def generar_archivo():
    try:
        data_to_write=[['CODIGO','PRODUCTO','STOCK'],
                       ['A100','XYZ',200],
                       ['A200','MNO',300],
                       ['A400','LXO',210],
                       ]
        with open("./UM_03/archivos/Archivo_Generate_Marzo03.csv",'w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data_to_write)
    except Exception as err:
        print(f"Error del Archivo {err}")   
    else:
        print("Se Genero el archivo correctamente")    
    finally:
        file.close()

generar_archivo()            
