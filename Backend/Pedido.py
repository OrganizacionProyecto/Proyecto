import mysql.connector
from Producto import Producto

class Pedido:
    def __init__(self, id, id_usuario, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.productos = []  # Lista para almacenar los productos en el pedido

    def agregarProducto(self, producto):
        # Agrega un producto al pedido
        self.productos.append(producto)

    def mostrarPedido(self):

        print(f"Pedido #{self.id}")
        print(f"Usuario: {self.id_usuario}")
        print(f"Estado: {self.estado}")
        print("Productos en el pedido:")
        for producto in self.productos:
            print(f"  - {producto.nombre}")

    def procesarPedido(self):
        self.estado = "Procesado"
        print(f"El pedido #{self.id} ha sido procesado.")

    def enviarMail(self):
        print(f"Se ha enviado un correo sobre el pedido #{self.id} al usuario.")

    def registrarPedido(self, conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para insertar un pedido en la base de datos
            sql = """
            INSERT INTO Pedido (id_usuario, estado)
            VALUES (%s, %s)
            """

            # Valores a insertar
            valores = (self.id_usuario, self.estado)

            # Ejecuta la sentencia SQL para insertar el pedido
            cursor.execute(sql, valores)

            # Obtiene el ID generado para el pedido
            self.id = cursor.lastrowid

            # Confirma los cambios en la base de datos
            conexion.commit()

            # Agregar relaciones entre pedido y productos en la tabla Pedido_Producto
            for producto in self.productos:
                sql_relacion = """
                INSERT INTO Pedido_Producto (pedido_id, producto_id)
                VALUES (%s, %s)
                """
                valores_relacion = (self.id, producto.id)
                cursor.execute(sql_relacion, valores_relacion)
                conexion.commit()

            print(f"Pedido #{self.id} insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar pedido en la base de datos: {error}")

    def eliminarPedido(self, conexion):
        try:
            cursor = conexion.obtener_cursor()
            sql = "DELETE FROM Pedido WHERE id = %s"

            # Valor a insertar (el ID del pedido a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            conexion.conexion.commit()

            print("Pedido eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar pedido de la base de datos: {error}")

    def obtenerProductosDelPedido(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para seleccionar productos asociados a un pedido
            sql = """
            SELECT Producto.* FROM Producto
            JOIN Pedido_Producto ON Producto.id = Pedido_Producto.producto_id
            WHERE Pedido_Producto.pedido_id = %s
            """
            cursor.execute(sql, (self.id,))
            productos_data = cursor.fetchall()

            productos = []
            for producto_data in productos_data:
                producto = Producto(*producto_data)
                productos.append(producto)

            return productos

        except mysql.connector.Error as error:
            print(f"Error al obtener productos del pedido: {error}")
            return []

    def mostrarTodosLosPedidos(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para seleccionar todos los pedidos
            sql = "SELECT * FROM Pedido"
            cursor.execute(sql)
            pedidos_data = cursor.fetchall()

            if not pedidos_data:
                print("No hay pedidos en la base de datos.")
            else:
                print("Lista de Pedidos:")
                for pedido_data in pedidos_data:
                    pedido = Pedido(*pedido_data)
                    # Agregar productos al pedido
                    productos = pedido.obtenerProductosDelPedido(conexion)
                    pedido.productos = productos
                    pedido.mostrarPedido()
                    print("\n")

        except mysql.connector.Error as error:
            print(f"Error al obtener la lista de pedidos: {error}")
