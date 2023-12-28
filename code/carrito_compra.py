articulos = {
    'vestido': 25,
    'zapatos': 30,
    'gorro': 10,
    'falda': 40,
}

carrito = []
print('productos disponibles')
for articulo , precio in articulos.items():
    print(f'{articulo}: ${precio}')

while True:
    nombre_articulo = input('Ingrese nombre de articulo (salir para finalizar)=>')
    if nombre_articulo == 'salir':
        break
    elif nombre_articulo in articulos:
        carrito.append(nombre_articulo)
        print(f"{nombre_articulo} agregado al carrito.")
    else:
        print("Producto no válido. Por favor, elige un producto válido.")
total_compra = 0
print("Resumen de la compra:")
for articulo in carrito:
    print(f"{articulo}: ${articulos[articulo]}")
    total_compra += articulos[articulo]

print(f"Total de la compra: ${total_compra}")

