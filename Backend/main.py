from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido
from Categoria import Categoria
from Conexion import Conexion
from Usuario import Usuario
from Administrador import Administrador

def mostrar_menu():
    print("Menu Principal:")
    print("1. Gestionar Clientes")
    print("2. Gestionar Categorias")
    print("3. Gestionar Productos")
    print("4. Gestionar Pedidos")
    print("5. Gestionar Usuarios")
    print("6. Gestionar Administradores")
    print("7. Salir del programa")

def main():
    # Configurar los datos de conexión a la base de datos
    host = "localhost"
    usuario = "root"
    contrasenia = "Andree.07"
    base_datos = "aymara"

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
                print("2. Eliminar Cliente")
                print("3. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    id = None
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    correo = input("Ingrese su correo: ")  
                    contrasenia = input("Ingrese su contraseña: ")  
                    domicilio = input("Ingrese su domicilio: ")
                    tipo = input("Ingrese 1 para ser Cliente: ")
                    usuario = Usuario(id, nombre, apellido, correo, contrasenia, domicilio, tipo)
                    usuario.registrarUsuario(conexion)
                    dni = input("Ingrese su DNI: ")
                    id_usuario = input("Asociar al usuario con Enter")
                    cliente = Cliente(id, usuario.nombre, usuario.apellido, usuario.correo, usuario.contrasenia, usuario.domicilio, usuario.tipo, dni, usuario.id)
                    cliente.registrarCliente(conexion)

                elif opcion == "2":
                    id = input("Ingrese un numero de Cliente: ")
                    cliente = Cliente(id, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None, dni=None, id_usuario=None)
                    cliente.eliminarCliente(conexion)

                elif opcion == "3":
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
                    id = input("Ingrese un numero de categoria: ")
                    nombre = input("Ingrese un nombre: ")
                    categoria = Categoria(id, nombre)
                    categoria.registrarCategoria(conexion)
                elif opcion == "2":
                    categoria = Categoria(id=None, nombre=None)
                    categoria.actualizarCategoria(conexion)
                elif opcion == "3":
                    id = input("Ingrese un numero de categoria: ")
                    categoria = Categoria(id, nombre=None)
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
                        id = None
                        nombre = input("Ingrese un nombre: ")
                        descripcion = input("Ingrese descripción: ")
                        precio = input("Ingrese un precio: ")
                        imagen = input("imagen: ")
                        stock = input("Nuevo stock (deje en blanco para mantener el valor actual): ")
                        categoria_id = input("Nuevo ID de categoría (deje en blanco para mantener el valor actual): ")
                        producto = Producto(id, nombre, descripcion, precio, imagen, stock, categoria_id)
                        producto.registrarProducto(conexion)
                    elif opcion == "2":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.actualizarProducto(conexion)
                    elif opcion == "3":
                        id = input("Ingrese un numero de Producto: ")
                        producto = Producto(id, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.eliminarProducto(conexion)
                    elif opcion == "4":
                        producto = Producto(id=None, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None)
                        producto.mostrarTodosLosProductos(conexion)
                    elif opcion == "5":
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
            
        if op == "4":
            while True:
                print("\nGestionar Pedidos:")
                print("1. Registrar Pedido")
                print("2. Actualizar Estado")
                print("3. Eliminar Pedido")
                print("4. Ver todos los pedidos")
                print("5. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    
                    while True:
                        usuario_id = input("Ingrese el ID del usuario que realiza el pedido: ")
                        usuario = Usuario.buscarUsuarioPorId(conexion, usuario_id)
                        if usuario:
                            estado = input("Ingrese el estado del pedido: ")  # Por ejemplo, "Pendiente"
                            nuevo_pedido = Pedido(id=None, id_usuario=usuario_id, estado=estado)
                            break
                        else:
                            print(f"No se encontró ningún producto con el ID {id_usuario}.")

                    while True:
                        producto_id = input("Ingrese el ID del producto a agregar al pedido (o Enter para finalizar): ")
                        if not producto_id:
                            break  # Sal del bucle si el usuario presiona Enter

                        producto = Producto.buscarProductoPorId(conexion, producto_id)
                        if producto:
                            nuevo_pedido.agregarProducto(producto)
                        else:
                            print(f"No se encontró ningún producto con el ID {producto_id}.")

                    nuevo_pedido.registrarPedido(conexion)

                elif opcion == "2":
                    # Modificar estado de un pedido
                    id_pedido = input("Ingrese el ID del pedido que desea modificar su estado: ")
                    pedido = Pedido(id=id_pedido, id_usuario=None, estado=None)
                    pedido.procesarPedido(conexion)


                elif opcion == "3":
                    # Eliminar un pedido
                    id_pedido = input("Ingrese el ID del pedido que desea eliminar: ")
                    pedido_a_eliminar = Pedido(id=id_pedido, id_usuario=None, estado=None)
                    pedido_a_eliminar.eliminarPedido(conexion)

                elif opcion == "4":
                    # Mostrar todos los pedidos
                    print("\nLista de Pedidos:")
                    pedido=Pedido(id=None, id_usuario=None, estado=None)
                    pedido.mostrarTodosLosPedidos(conexion)
                elif opcion == "5":
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")

                        
        if op == "5":
            while True:   
                print("\nGestionar usuarios:")
                print("1. Registrar Usuario")
                print("2. Iniciar sesión")
                print("3. Eliminar Usuario")
                print("4. Actualizar usuario")
                print("5. Mostrar Usuarios")
                print("6. Actualizar contraseña")
                print("7. Volver al menu principal")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    correo = input("Ingrese su correo: ")  
                    contrasenia = input("Ingrese su contraseña: ") 
                    domicilio = input("Ingrese su domicilio: ")
                    tipo=input("Tipo de usuario: ")
                    usuario = Usuario (nombre, apellido, correo, contrasenia, domicilio, tipo)
                    usuario.registrarUsuario(conexion)
                elif opcion == "2":
                    correo = input("Ingrese su correo: ")
                    contrasenia = input("Ingrese su contraseña: ")
                    usuario = Usuario(id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    if usuario.iniciarSesion(correo, contrasenia, conexion):
                        # Inicio de sesión exitoso
                        print(f"Bienvenido, {usuario.nombre} {usuario.apellido}!")
                    else:
                        # Inicio de sesión fallido
                        print("Credenciales incorrectas. Inicio de sesión fallido.")
                        
                elif opcion == "3":
                    id = input("Ingrese el ID del usuario a eliminar: ")
                    usuario = Usuario(nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.eliminarUsuario(conexion, id)
                    
                elif opcion == "4":
                    usuario = Usuario (nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.actualizarUsuario(conexion)
                elif opcion == "5":
                    usuario = Usuario(nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.mostrarTodosLosUsuarios(conexion)
                elif opcion == "6":
                    usuario = Usuario(id=None, nombre=None, apellido=None, correo=None, contrasenia=None, domicilio=None, tipo=None)
                    usuario.actualizarContrasenia(conexion)
                elif opcion == "7":
                    break
                            
        if op == "6":
             while True:   
                print("\nGestionar Administradores:")
                print("1. Registrar Administrador a traves de id de usuario")
                print("2. Volver al Menú Principal")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    id_usuario = input("Ingrese id de usuario: ")
                    administrador = Administrador(id = None, nombre = None, apellido = None, correo = None, contrasenia = None, domicilio = None, tipo=None, id_usuario=id_usuario)
                    administrador.registrarAdmin(conexion)
                elif opcion == "2":
                    break

        if op == "7":
            break
        if op != "1" and "2" and "3" and "4" and "5" and "6" and "7":
            print("Opcion no valida, ingrese una que sea valida")

    conexion.cerrar() 

if __name__ == "__main__":
    main()
