productos = {
    "azucar": 10,
    "arroz": 20,
    "sal": 30,
    "aceite": 12,
    "vinagre": 10,
}
carrito = []
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")


while True:
    seleccion = input("Selecciona un producto para agregar al carrito (o 'salir' para finalizar): ")

    if seleccion == 'salir':
        break
    elif seleccion in productos:
        carrito.append(seleccion)
        print(f"{seleccion} agregado al carrito.")
    else:
        print("Producto no válido. Por favor, elige un producto válido.")


total_compra = 0
print("\nResumen de la compra:")
for producto in carrito:
    print(f"{producto}: ${productos[producto]}")
    total_compra += productos[producto]

print(f"Total de la compra: ${total_compra}")