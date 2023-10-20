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

class Producto:

    def registrarProducto(self, conexion):
        try:
                cursor = conexion.obtener_cursor()

                sql = """
                INSERT INTO Producto (nombre, descripcion, precio, imagen, stock, categoria_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

                # Valores a insertar
                valores = (self.nombre, self.descripcion, self.precio, self.imagen, self.stock, self.categoria_id)

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
            nombre = input("Nuevo nombre (deje en blanco para mantener el valor actual): ")
            descripcion = input("Nueva descripción (deje en blanco para mantener el valor actual): ")
            precio = input("Nuevo precio (deje en blanco para mantener el valor actual): ")
            imagen = input("Nueva imagen (deje en blanco para mantener el valor actual): ")
            stock = input("Nuevo stock (deje en blanco para mantener el valor actual): ")
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
            conexion.commit()

            print(f"Producto ID {producto_id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar producto en la base de datos: {error}")



    def eliminarProducto(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Solicitar al usuario el ID del producto a eliminar
            producto_id = input("Ingrese el ID del producto que desea eliminar: ")

            # Verificar si el producto con el ID proporcionado existe en la base de datos
            cursor.execute("SELECT id FROM Producto WHERE id = %s", (producto_id,))
            producto = cursor.fetchone()

            if not producto:
                print(f"No se encontró ningún producto con el ID {producto_id}.")
                return

            # Define la sentencia SQL para eliminar un producto de la base de datos
            sql = "DELETE FROM Producto WHERE id = %s"

            # Valor a insertar (el ID del producto a eliminar)
            valor = (producto_id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print(f"Producto con ID {producto_id} eliminado de la base de datos")

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

    def menu_producto(self, conexion):
        while True:
            print("Menu de Productos:")
            print("1. Registrar Producto")
            print("2. Actualizar Producto")
            print("3. Eliminar Producto")
            print("4. Mostrar Todos los Productos")
            print("5. Volver al Menú Principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrarProducto(conexion)
            elif opcion == "2":
                self.actualizarProducto(conexion=conexion)
            elif opcion == "3":
                self.eliminarProducto(conexion)
            elif opcion == "4":
                self.mostrarTodosLosProductos(conexion)
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

