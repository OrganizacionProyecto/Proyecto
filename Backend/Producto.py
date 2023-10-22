import mysql.connector
from Conexion import Conexion

class Producto:
    def __init__(self, id, nombre, descripcion, precio, imagen, stock, categoria_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen
        self.stock = stock
        self.categoria_id = categoria_id


    def registrarProducto(self, conexion):
        try:
            cursor = conexion.obtener_cursor()  

            # Define la sentencia SQL para insertar un producto en la base de datos
            sql = """
            INSERT INTO Producto (id, nombre, descripcion, precio, imagen, stock, categoria_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            # Valores a insertar
            valores = (self.id, self.nombre, self.descripcion, self.precio, self.imagen, self.stock, self.categoria_id)

                # Ejecuta la sentencia SQL
                cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

                print("Producto insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar producto en la base de datos: {error}")
            
            
    def actualizarProducto(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Solicitar al usuario el ID del producto a actualizar
            producto_id = input("Ingrese el ID del producto que desea actualizar: ")

            # Verificar si el producto con el ID proporcionado existe en la base de datos
            cursor.execute("SELECT id FROM Producto WHERE id = %s", (producto_id,))
            producto = cursor.fetchone()

            if not producto:
                print(f"No se encontró ningún producto con el ID {producto_id}.")
                return

            # Define la sentencia SQL para actualizar un producto en la base de datos
            sql = """
            UPDATE Producto
            SET nombre = %s, descripcion = %s, precio = %s, imagen = %s, stock = %s, categoria_id = %s
            WHERE id = %s
            """

            # Solicitar al usuario los nuevos valores
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            precio = input("Nuevo precio: ")
            imagen = input("Nueva imagen (deje en blanco para mantener el valor actual): ")
            stock = input("Nuevo stock: ")
            categoria_id = input("Nuevo ID de categoría (deje en blanco para mantener el valor actual): ")

            # Valores a actualizar
            valores = (
                nombre if nombre else self.nombre,
                descripcion if descripcion else self.descripcion,
                precio if precio else self.precio,
                imagen if imagen else self.imagen,
                stock if stock else self.stock,
                categoria_id if categoria_id else self.categoria_id,
                producto_id
            )

            # Ejecuta la sentencia SQL para actualizar el producto
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print(f"Producto ID {producto_id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar producto en la base de datos: {error}")

    def eliminarUsuario(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Verifica si existen pedidos asociados a este usuario
            sql_check_pedido = "SELECT COUNT(*) FROM Pedido WHERE id_usuario = %s"
            cursor.execute(sql_check_pedido, (self.id,))
            count = cursor.fetchone()[0]

            if count > 0:
                print("No se puede eliminar el usuario porque está asociado a pedidos.")
            else:
                # Si no está asociado a ningún pedido, procede a eliminar el usuario
                sql = "DELETE FROM Usuario WHERE id = %s"
                valor = (self.id,)
                cursor.execute(sql, valor)
                conexion.conexion.commit()

                print("Usuario eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar usuario de la base de datos: {error}")
            try:
                cursor = conexion.obtener_cursor()

                # Primero, verifica si el producto está asociado a algún pedido
                sql_check_pedido = "SELECT COUNT(*) FROM Pedido_Producto WHERE producto_id = %s"
                cursor.execute(sql_check_pedido, (self.id,))
                count = cursor.fetchone()[0]

                if count > 0:
                    print("No se puede eliminar el producto porque está asociado a pedidos.")
                else:
                    # Si no está asociado a ningún pedido, procede a eliminar el producto
                    sql = "DELETE FROM Producto WHERE id = %s"
                    valor = (self.id,)
                    cursor.execute(sql, valor)
                    conexion.conexion.commit()

                    print("Producto eliminado de la base de datos")

            except mysql.connector.Error as error:
                print(f"Error al eliminar producto de la base de datos: {error}")
    def mostrarProducto(self):
        # Muestra la información del producto.
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio: ${self.precio}")
        print(f"Imagen: {self.imagen}")
        print(f"Stock: {self.stock}")
        print(f"Categoría ID: {self.categoria_id}")

    def mostrarTodosLosProductos(self, conexion):
            try:
                cursor = conexion.obtener_cursor()

                # Define la sentencia SQL para seleccionar todos los productos
                sql = "SELECT * FROM Producto"
                cursor.execute(sql)
                productos = cursor.fetchall()

                if not productos:
                    print("No hay productos en la base de datos.")
                else:
                    print("Lista de Productos:")
                    for producto in productos:
                        producto_obj = Producto(*producto)
                        producto_obj.mostrarProducto()
                        print("\n")

            except mysql.connector.Error as error:
                print(f"Error al obtener la lista de productos: {error}")

    def buscarProductoPorId(conexion, producto_id):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para buscar un producto por ID
            sql = "SELECT * FROM Producto WHERE id = %s"
            cursor.execute(sql, (producto_id,))
            producto_data = cursor.fetchone()

            if producto_data:
                # Si se encontró un producto con el ID proporcionado, crea un objeto Producto
                producto = Producto(*producto_data)
                return producto
            else:
                return None  # No se encontró ningún producto con ese ID

        except mysql.connector.Error as error:
            print(f"Error al buscar producto por ID: {error}")
            return None