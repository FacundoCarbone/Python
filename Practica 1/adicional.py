def mostrar_inventario(invntario):
    if not inventario:
        print('El inventario esta vacio')
    else:
        print('\nInventario actual: ')
        for producto,cantidad in inventario.items():
            print(f'{producto}:{cantidad}')
def agregar_producto(inventario):
    nombre= input('Ingrese el nombre del producto: ')
    if nombre in inventario:
        print('El producto ya se encuentra en el inventario')
    cantidad=int(input('Ingrese la cantidad :'))
    inventario[nombre]=inventario.get(nombre,0)+ cantidad 
    print(f'producto{nombre} agregado con {cantidad}')

def eliminar_producto(inventario):
    nombre=input('Ingrese el producto a eliminar: ')
    if nombre in inventario:
        del inventario[nombre]
        print(f'{nombre} eliminado del inventario')
    else:
        print(f'{nombre}no se encontro en el diccionario')

inventario= {}
while True:
    print('Seleccionar una opcion:')
    print('1, agregar producto')
    print('2, eliminar producto')
    print('3, mostrar inventario')
    print('4,salir')

    opcion= int(input('Opcion: '))
    if opcion == 1:
        agregar_producto(inventario)
    elif opcion == 2:
        eliminar_producto(inventario)
    elif opcion == 3:
        mostrar_inventario(inventario)
    elif opcion == 4:
        print('Saliendo del programa')
        break
    else:
        print('La opcion ingresada no es valida')
