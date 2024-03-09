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

