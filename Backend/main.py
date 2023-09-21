from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido
from Categoria import Categoria
from Conexion import Conexion

def mostrar_menu():
    print("Menu Principal:")
    print("1. Gestionar Clientes")
    print("2. Gestionar Categorias")
    print("3. Gestionar Productos")
    print("4. Gestionar Pedidos")
    print("5. Salir del programa")

def main():
    # Configurar los datos de conexión a la base de datos
    host = "localhost"
    usuario = "root"
    contrasenia = ""
    base_datos = "aymara"

    # Crear una instancia de la clase Conexion
    conexion = Conexion(host, usuario, contrasenia, base_datos)

    # Conectar a la base de datos
    conexion.conectar()

    while True:
        mostrar_menu()
        op = input("Seleccione una opcion: ")
        if op == "1":
            """Gestionar Clientes"""
            pass
        if op == "2":
            """Gestionar Categorias"""
            pass
        if op == "3":
            """Gestionar Producto"""
            pass
        if op == "4":
            """Gestionar Pedidos"""
            pass
        if op == "5":
            """Salir"""
            break
        else:
            print("Opcion no valida, ingrese una que sea valida")


# Cerrar la conexión a la base de datos
    conexion.cerrar()

if __name__ == "__main__":
    main()
