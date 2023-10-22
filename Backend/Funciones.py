from Cliente import Cliente
from Categoria import Categoria

def OpMenu():
    
    while True:
        print("Menu Principal:")
        print("1. Gestionar Clientes")
        print("2. Gestionar Categorias")
        print("3. Gestionar Productos")
        print("4. Gestionar Pedidos")
        print("5. Salir del programa")
        op = input("Seleccione una opcion: ")
        if op == "1":
            pass
            
        if op == "2":
            menuCategoria()
        if op == "3":
            """Gestionar Producto"""
            pass
        if op == "4":
            """Gestionar Pedidos"""
            pass
        if op == "5":
            """Salir"""
            break
        if op != "1" and op != "2" and op != "3" and op != "4" and op != "5":
            print("Opcion no valida, ingrese una que sea valida")

def menuCategoria():
    
    while True:
        print("Menu Categoria:")
        print("1. Registrar Categoria")
        print("2. Eliminar Categoria")
        print("3. Gestionar Productos")
        print("4. Gestionar Pedidos")
        print("5. Salir del programa")
        op = input("Seleccione una opcion: ")
        if op == "1":
            nombre = input("Ingrese el nombre de la categoria: ")
            categoria = Categoria(id, nombre)
            categoria.registrarCategoria()
        if op == "2":
            nombre = input("Ingrese el nombre de la categoria")
            categoria = Categoria(id, nombre)
        if op == "3":
            """Gestionar Producto"""
            pass
        if op == "4":
            """Gestionar Pedidos"""
            pass
        if op == "5":
            """Salir"""
            break
        if op != "1" and op != "2" and op != "3" and op != "4" and op != "5":
            print("Opcion no valida, ingrese una que sea valida")