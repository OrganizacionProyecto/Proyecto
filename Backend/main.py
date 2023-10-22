from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido
from Categoria import Categoria
from Conexion import Conexion
from Administrador import Administrador
from Usuario import Usuario
def mostrar_menu():
    print("Menu Principal:")
    print("1. Gestionar Clientes")
    print("2. Gestionar Categorias")
    print("3. Gestionar Productos")
    print("4. Gestionar Pedidos")
    print("5. Gestionar Administradores")
    print("6. Gestionar Usuarios")
    print("7. Salir del programa")

def main():
    # Configurar los datos de conexión a la base de datos
    host = "localhost"
    usuario = "root"
    contrasenia = "root"
    base_datos = "aymara"

    # Crear una instancia de la clase Conexion
    conection = Conexion(host, usuario, contrasenia, base_datos)

    # Conectar a la base de datos
    conection.conectar()
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
                    dni = input("Ingrese su DNI: ")
                    contrasenia = input("Ingrese su contraseña: ")  
                    domicilio = input("Ingrese su domicilio: ")
                    cliente = Cliente(id, nombre, apellido, correo, dni, contrasenia, domicilio)
           
                    cliente.registrarCliente(conection)
                elif opcion == "2":
                   cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, dni=None, contrasenia=None, domicilio=None)
                   cliente.iniciarSesion(conection, contrasenia=None)
                elif opcion == "3":
                    cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, dni=None, contrasenia=None, domicilio=None)
                    cliente.eliminarCliente(conection)
                elif opcion == "4":
                    cliente = Cliente(id=None, nombre=None, apellido=None, correo=None, dni=None, contrasenia=None, domicilio=None)
                    cliente.actualizarCliente(conection)
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
                    categoria.registrarCategoria(conection)
                elif opcion == "2":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.actualizarCategoria(conection)
                elif opcion == "3":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.eliminarCategoria(conection)
                elif opcion == "4":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.mostrar_todas_las_categorias(conection)
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
                        stock = input("Ingrese stock: ")
                        categoria_id = input("ID de categoría ")
                        producto = Producto(id, nombre, descripcion, precio, imagen, stock, categoria_id=None)
                        producto.registrarProducto(conection)
                    elif opcion == "2":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.actualizarProducto(conection)
                    elif opcion == "3":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.eliminarProducto(conection)
                    elif opcion == "4":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.mostrarTodosLosProductos(conection)
                    elif opcion == "5":
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
            
        if op == "4":
             while True:   
                print("\nGestionar Pedido:")
                print("1. Registrar Pedido")
                opcion = input("Seleccione una opción: ")
        
        if op == "5":
             while True:   
                print("\nGestionar Administradores:")
                print("1. Registrar Administrador a traves de id de usuario")
                print("2. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    id_usuario = input("Ingrese id de usuario: ")
                    administrador = Administrador(id = None, nombre = None, apellido = None, correo = None, contrasenia = None, domicilio = None, tipo=None, id_usuario=id_usuario)
                    administrador.registrarAdmin(conection)
                elif opcion == "2":
                    break

                
        if op == "6":
            while True:   
                print("\nGestionar usuarios:")
                print("Seccion en construccion")
                print("1. Registrar Usuario")
                print("2. Iniciar sesión")
                print("3. Eliminar Usuario")
                print("4. Actualizar usuario")
                print("5. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    correo = input("Ingrese su correo: ")  
                    contrasenia = input("Ingrese su contraseña: ") 
                    domicilio = input("Ingrese su domicilio: ")
                    tipo=input("Tipo de usuario: ")
                    usuario = Usuario (id, nombre, apellido, correo, contrasenia, domicilio, tipo)
                    usuario.registrarUsuario(conection)
                elif opcion == "2":
                   usuario = Usuario (id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                   usuario.iniciarSesion(conection, contrasenia=None)
                elif opcion == "3":
                    usuario = Usuario (id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.eliminarUsuario(conection)
                elif opcion == "4":
                    usuario = Usuario (id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.actualizarUsuario(conection)
                elif opcion == "5":
                    break
                    
        if op == "7":
            break
        if op != "1" and "2" and "3" and "4" and "5" and "6" and "7":
            print("Opcion no valida, ingrese una que sea valida")

    conection.cerrar() 

if __name__ == "__main__":
    main()
