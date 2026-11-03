catalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de micropuntas", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Resma de papel", "precio": 15000, "stock": 8}
}


def buscar():
    codigo = input("Codigo del producto: ").upper()
    producto = catalogo.get(codigo)

    if producto == None:
        print("ADVERTENCIA: ese codigo no existe")
        print("Codigos disponibles:", list(catalogo.keys()))
    else:
        print("Datos del producto", codigo)
        for dato, valor in producto.items():
            print(dato, ":", valor)


def agregar_stock():
    codigo = input("Codigo del producto: ").upper()

    if codigo in catalogo:
        cantidad = input("Cantidad que llega: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            catalogo[codigo]["stock"] += int(cantidad)
            print("Nuevo stock:", catalogo[codigo]["stock"])
        else:
            print("Cantidad no valida")
    else:
        print("ADVERTENCIA: ese codigo no existe")


def nuevo_producto():
    codigo = input("Codigo nuevo: ").upper()

    if codigo in catalogo:
        print("ADVERTENCIA: ese codigo ya existe")
        respuesta = input("Desea sobreescribirlo? (s/n): ")
        if respuesta != "s":
            print("No se hizo ningun cambio")
            return

    nombre = input("Nombre: ")
    precio = input("Precio: ")
    stock = input("Stock: ")

    if nombre == "" or precio.isdigit() == False or stock.isdigit() == False:
        print("Datos no validos")
    else:
        catalogo.update({codigo: {"nombre": nombre, "precio": int(precio), "stock": int(stock)}})
        print("Producto guardado")


def valor_inventario():
    total = 0
    for producto in catalogo.values():
        total = total + producto["precio"] * producto["stock"]
    print("Valor total del inventario: $", total)


opcion = ""
while opcion != "5":
    print("\n--- CATALOGO DE TIENDA ---")
    print("1. Buscar producto")
    print("2. Ingresar existencias")
    print("3. Registrar producto nuevo")
    print("4. Valor del inventario")
    print("5. Salir")
    opcion = input("Opcion: ")

    if opcion == "1":
        buscar()
    elif opcion == "2":
        agregar_stock()
    elif opcion == "3":
        nuevo_producto()
    elif opcion == "4":
        valor_inventario()
    elif opcion == "5":
        print("Hasta luego")
    else:
        print("Opcion no valida")
