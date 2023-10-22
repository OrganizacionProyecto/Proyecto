from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido
from Categoria import Categoria
from Conexion import Conexion
from Usuario import Usuario

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
    contrasenia = "root"
    base_datos = "aymara_db"

    # Crear una instancia de la clase Conexion
    conexion = Conexion(host, usuario, contrasenia, base_datos)

    # Conectar a la base de datos
    conexion.conectar()
    while True:
        mostrar_menu()
        op = input("Seleccione una opcion: ")
        if op == "1":
             while True:   
                print("\nGestionar Clientes:")
                print("1. Registrar Cliente")
                print("2. Iniciar sesion")
                print("3. Eliminar Cliente")
                print("4. Actualizar cliente")
                print("5. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    correo = input("Ingrese su correo: ")  
                    contrasenia = input("Ingrese su contraseña: ")  
                    domicilio = input("Ingrese su domicilio: ")
                    tipo = input("Ingrese su DNI: ")
                    usuario = Usuario(id, nombre, apellido, correo, contrasenia, domicilio, tipo)
                    usuario.registrarUsuario(conexion)
                    dni = input("Ingrese su DNI: ")
                    id_usuario = input("Asociar al usuario con Enter")
                    cliente = Cliente(id, dni, id_usuario)
                    cliente.registrarCliente(conexion)
                elif opcion == "2":
                   cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, dni=None, id_usuario=None)
                   cliente.iniciar_sesion(conexion)
                elif opcion == "3":
                    cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, dni=None, id_usuario=None)
                    cliente.eliminarCliente(conexion)
                elif opcion == "4":
                    cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, dni=None, id_usuario=None)
                    cliente.actualizarCliente(conexion)
                elif opcion == "5":
                    break
            
        if op == "2":
            while True:
                print("\nGestionar Categorías:")
                print("1. Registrar Categoría")
                print("2. Actualizar Categoría")
                print("3. Eliminar Categoría")
                print("4. Mostrar Todas las Categorías")
                print("5. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nombre = input("Ingrese un nombre: ")
                    categoria = Categoria(id, nombre)
                    categoria.registrarCategoria(conexion)
                elif opcion == "2":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.actualizarCategoria(conexion)
                elif opcion == "3":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.eliminarCategoria(conexion)
                elif opcion == "4":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.mostrar_todas_las_categorias(conexion)
                elif opcion == "5":
                    break
            
            
            
        if op == "3":
                
                while True:
                    print("Menu de Productos:")
                    print("1. Registrar Producto")
                    print("2. Actualizar Producto")
                    print("3. Eliminar Producto")
                    print("4. Mostrar Todos los Productos")
                    print("5. Volver al Menú Principal")
                
                    opcion = input("Seleccione una opción: ")
                
                    if opcion == "1":
                        nombre = input("Ingrese un nombre: ")
                        descripcion = input("Ingrese descripción: ")
                        precio = input("Ingrese un precio: ")
                        imagen = input("imagen: ")
                        stock = input("Nuevo stock (deje en blanco para mantener el valor actual): ")
                        #categoria_id = input("Nuevo ID de categoría (deje en blanco para mantener el valor actual): ")
                        producto = Producto(id, nombre, descripcion, precio, imagen, stock, categoria_id=None)
                        producto.registrarProducto(conexion)
                    elif opcion == "2":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.actualizarProducto(conexion)
                    elif opcion == "3":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.eliminarProducto(conexion)
                    elif opcion == "4":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.mostrarTodosLosProductos(conexion)
                    elif opcion == "5":
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
            
        if op == "4":
            """Gestionar Pedidos"""
            print("Seccion en trabajo, se realizara el cuatrimestre que sigue")
            return
        if op == "5":
            break
        if op != "1" and "2" and "3" and "4" and "5":
            print("Opcion no valida, ingrese una que sea valida")

    conexion.cerrar() 

if __name__ == "__main__":
    main()