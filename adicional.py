def mostrar_inventario(inventario):
    if not inventario:
        print('inventario vacio')
    else:
        print('\nInventario Actual: ')
        for producto, cantidad in inventario.items():
            print(f'{producto}:{cantidad}')

def agregar_producto(inventario):
    nombre=input ('Ingrese el nombre del producto: ')
    if nombre in inventario:
        print('el producto ya se encuentra, se actualizara la cantidad')
    cantidad=int(input('ingrese la cantidad: '))
    inventario [nombre]=inventario.get(nombre,0)+ cantidad

def eliminar_producto(inventario):
    nombre=input('ingrese el nombre dle producto a eliminar: ')
    if nombre in inventario:
        del inventario[nombre]
        print('producto eliminado')
    else:
        print('el producto no estaba en el inventario')


inventario={}
while True:
    print('\nSeleccione una opcion: ')
    print('1,agregar producto')
    print('2, eliminar produto')
    print('3,mostrar inventario')
    print('4,salir')
    opcion=int(input('opcion: '))
    if opcion == 1:
        agregar_producto(inventario)
    elif opcion == 2 :
        eliminar_producto(inventario)
    elif opcion == 3:
        mostrar_inventario(inventario)
    elif opcion == 4:   
        break
    else:
        print('opcion no valida')