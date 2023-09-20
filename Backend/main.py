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

    try:
        # Crear un cliente y guardar en la base de datos
        
        #cliente1 = Cliente(None, "Pedro", "Gomez", "Pedro@example.com", 123456789, "contraseña123", "123 Calle Principal")
        #cliente1.registrarCliente(conexion.conexion)

        # Crear una categoria y guardar en la base de datos
        #categoria1 = Categoria(None, "Categoria 1")
        #categoria1.registrarCategoria(conexion.conexion)


        # Crear un producto y guardar en la base de datos
        producto1 = Producto(None, "Producto 3", "Descripción del Producto 3", 19.99, "imagen3.jpg", 100, 1)
        #producto2 = Producto(None, "Producto 4", "Descripción del Producto 4", 29.99, "imagen4.jpg", 200, 1)
        producto1.registrarProducto(conexion.conexion)

        # Crear un pedido y agregar productos al pedido
        #pedido1 = Pedido(None, cliente1.id, "Pendiente")
        #pedido1.agregarProducto(producto1)
        #pedido1.agregarProducto(producto2)
        # Guardar el pedido en la base de datos
        #pedido1.registrarPedido(conexion.conexion)



        # Crear un pedido y agregar un producto al pedido
        #pedido1 = Pedido(None, cliente1.id, "Pendiente")
        #pedido1.agregarProducto(producto)

        # Guardar el pedido en la base de datos
        #pedido1.registrarPedido(conexion.conexion)

    except Exception as e:
        print(f"Error al interactuar con la base de datos: {str(e)}")

    # Cerrar la conexión a la base de datos
    conexion.cerrar()

if __name__ == "__main__":
    main()
