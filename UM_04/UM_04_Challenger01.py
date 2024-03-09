"""
El objetivo de este proyecto es crear un programa en Python que simule un carrito de compras. El carrito debe permitir al usuario agregar productos, ver el contenido actual del carrito y realizar el pago. La información de los productos estará almacenada en un archivo CSV.

Estructura del Archivo CSV:

1.-El archivo CSV contendrá información sobre los productos disponibles para comprar.
Cada fila del archivo representará un producto y contendrá al menos los siguientes campos: "ID", "Nombre", "Precio".
Puedes agregar más campos según sea necesario (por ejemplo, "Stock", "Descripción", etc.).
2.Funcionalidades del Carrito:
-Agregar Producto al Carrito: El programa debe permitir al usuario agregar productos al carrito indicando el ID del producto y la cantidad deseada.
-Ver Contenido del Carrito: El usuario puede ver el contenido actual del carrito, incluyendo los productos, cantidades y el total a pagar.
-Realizar Pago: Una vez que el usuario ha terminado de agregar productos al carrito, debe poder realizar el pago. Esto deberá mostrar el total a pagar y restar la cantidad de productos comprados del stock.

Requisitos Adicionales:
=========================
-Debes manejar situaciones donde el usuario intenta agregar una cantidad mayor que la disponible en el stock.
-El programa debe proporcionar retroalimentación adecuada al usuario en cada operación realizada.(usar excepciones)
"""
import csv

def cargar_productos():
    try:
        with open('./UM_04/archivos/productos.csv','r') as file:
            reader = csv.DictReader(file)  
            productos=list(reader)
            return productos
    except Exception as err:
        return f"Ocurrio un Error {err}"    
    
def mostrar_productos(productos):
    print("Productos Disponibles")
    for producto in productos:
        print(f"{producto['ID']}: {producto['NOMBRE']} - ${str(producto['PRECIO'])} - {producto['STOCK']}")

def agregar_carrito(carrito,productos,producto_id,cantidad):
    
    for producto in productos:
        if producto["ID"]==producto_id:
            stock_disponible=int(producto['STOCK'])
            if cantidad<=stock_disponible:
                carrito.append({
                    'ID':producto['ID'],
                    'NOMBRE':producto['NOMBRE'],
                    'PRECIO':float(producto['PRECIO']),
                    'CANTIDAD':cantidad
                })
                producto['STOCK']=str(stock_disponible-cantidad)
                print(f"Producto Agregado al carrito {producto['NOMBRE']} X {cantidad}")
            else:
                print("No Hay Stock Suficiente")        
            return
    print("Producto No Disponible")    
              
def ver_carrito(carrito):
    total=sum(item['PRECIO'] * item['CANTIDAD']for item in carrito)
    print("\nContenido del Carrito")
    for item in carrito:
        print(f"{item['NOMBRE']} x {item['CANTIDAD']} - ${item['PRECIO']*item['CANTIDAD']:.2f}")
    print(f"\nTotal a Pagar ${total:.2f}\n")    

def main():
    productos=cargar_productos()
    carrito=[]
    while True:
        mostrar_productos(productos)
        opcion=input("\n1.-Agregar Al Carrito\n2.-Ver Carrito\n3.-Realizar Pago\n4.-Salir\n")
        if opcion =='1':
            producto_id=input("Ingrese el codigo a comprar:")
            cantidad=int(input("Ingrese la cantidad:"))
            agregar_carrito(carrito,productos,producto_id,cantidad)
        elif opcion=='2':
            ver_carrito(carrito)    
        elif opcion =='3':
            print("Realizar Pago")    
        elif opcion=='4':
            break
        else:
            print("Opcion No valida Intente de nuevo")

if __name__ =='__main__':
    main()
