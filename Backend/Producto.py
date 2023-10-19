import mysql.connector

class Producto:
    def __init__(self, id, nombre, descripcion, precio, imagen, stock, categoria_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen
        self.stock = stock
        self.categoria_id = categoria_id

    import mysql.connector

class Producto:


    def registrarProducto(self, conexion):
        try:
            cursor = conexion.cursor()  # Obtén un cursor a partir de la conexión

            # Define la sentencia SQL para insertar un producto en la base de datos
            sql = """
            INSERT INTO Producto (nombre, descripcion, precio, imagen, stock, categoria_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            # Valores a insertar
            valores = (self.nombre, self.descripcion, self.precio, self.imagen, self.stock, self.categoria_id)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print("Producto insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar producto en la base de datos: {error}")


    def actualizarProducto(self, nombre=None, descripcion=None, precio=None, imagen=None, stock=None, categoria_id=None, conexion=None):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para actualizar un producto en la base de datos
            sql = """
            UPDATE Producto
            SET nombre = %s, descripcion = %s, precio = %s, imagen = %s, stock = %s, categoria_id = %s
            WHERE id = %s
            """

            # Valores a actualizar
            valores = (
                nombre if nombre is not None else self.nombre,
                descripcion if descripcion is not None else self.descripcion,
                precio if precio is not None else self.precio,
                imagen if imagen is not None else self.imagen,
                stock if stock is not None else self.stock,
                categoria_id if categoria_id is not None else self.categoria_id,
                self.id
            )

            # Ejecuta la sentencia SQL para actualizar el producto
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print(f"Producto ID {self.id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar producto en la base de datos: {error}")


    def eliminarProducto(self,conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Producto WHERE id = %s"

            # Valor a insertar (el ID del producto a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.commit()

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
            cursor = conexion.cursor()
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


    def obtenerCategoria(self):
        # Implementa la lógica para obtener la categoría de un producto.
        pass

    def modificarCategoria(self):
        # Implementa la lógica para modificar la categoría de un producto.
       pass

