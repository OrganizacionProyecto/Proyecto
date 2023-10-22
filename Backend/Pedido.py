import mysql.connector

class Pedido:
    def __init__(self, id, id_usuario, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.estado = estado
        self.productos = []  # Lista para almacenar los productos en el pedido
        

    def agregarProducto(self, productos):
        # Agrega un producto al pedido
        self.productos.append(productos)

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
            cursor = conexion.obtener_cursor()

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
            conexion.conexion.commit()

            # Agregar relaciones entre pedido y productos en la tabla Pedido_Producto
            for producto in self.productos:
                sql_relacion = """
                INSERT INTO Pedido_Producto (pedido_id, producto_id)
                VALUES (%s, %s)
                """
                valores_relacion = (self.id, producto.id)
                cursor.execute(sql_relacion, valores_relacion)
                conexion.conexion.commit()

            print(f"Pedido #{self.id} insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar pedido en la base de datos: {error}")
    
    def eliminarPedido(self,conexion):
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM Pedido WHERE id = %s"
            valor = (self.id,)
            cursor.execute(sql, valor)
            conexion.commit()

            print("Pedido eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar pedido de la base de datos: {error}")