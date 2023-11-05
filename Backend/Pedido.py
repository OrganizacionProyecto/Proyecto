import mysql.connector
from Producto import Producto

class Pedido:
    def __init__(self, id, id_usuario, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.estado = estado
        self.productos = []  # Lista para almacenar los productos en el pedido

    def agregarProducto(self, producto):
        # Agrega un producto al pedido
        self.productos.append(producto)

## el siguiente comentario es proyeccion para ingresar un valor a los envios de pedidos
    # def provincia(self): #aca lo usamos para que saber de que provincia es, debería acceder al domicilio y ver si "contiene" la prinvincia en el dom.
    #         domicilio = self.cliente.domicilio #acca accederia a la clase cliente...
    #         provincias = {          #array
    #             "Cordoba": 0,
    #             "Buenos Aires": 700,
    #             "Chaco": 1000,
    #             "Formosa": 800,
    #             # podemos seguir agregando pero para ver si lo dejamos lo dejo ahi
    #         }

    #         for provincia, precio in provincias.items():
    #             if provincia in domicilio: #si encuentra dentro del domicilio la provincia que esta en la lista
    #                 return provincia, precio  #devuelve la procinvia y el precio y sino imprime

    #         return "No encontrada", 0  # en lugar de provincia devuelve otra cosa y precio $0
        
    # def envio(self):
    #     provincia, precio = self.provincia()
    #     if provincia == "No encontrada":
    #         print("Lo sentimos, no ofrecemos servicio de envío en tu provincia.")
    #     else:
    #         print(f"Provincia: {provincia}, Precio de Envío: ${precio}")

    def mostrarPedido(self):
        print(f"Pedido #{self.id}")
        print(f"Usuario: {self.id_usuario}")
        print(f"Estado: {self.estado}")
        print("Productos en el pedido:")
        for producto in self.productos:
            print(f"  - {producto.nombre}")

    def procesarPedido(self,id, estado, conexion):
         try:
            cursor = conexion.obtener_cursor()
            id = input("Ingrese el ID del pedido a acualizar: ")

            # Verificar si el producto con el ID proporcionado existe en la base de datos
            cursor.execute("SELECT id FROM PEDIDO WHERE id = %s", (id,))
            pedido = cursor.fetchone()

            if not pedido:
                print(f"No se encontró ningún pedido con el ID {id}.")
                return


            # Define la sentencia SQL para actualizar la contraseña de un cliente en la base de datos
            sql = """
            UPDATE pedido
            SET estado = %s
            WHERE id = %s
            """
        
 
            # Valores a actualizar
            valores = (
                estado if estado  else self.estado,
                id
            )

            # Ejecuta la sentencia SQL para actualizar el cliente
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print(f"El estado del Pedido ID {self.id} ha sido actualizada en la base de datos")

         except mysql.connector.Error as error:
            print(f"Error al actualizar el estado del pedido en la  base de datos: {error}")
    
       

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

    def eliminarPedido(self, conexion):
        try:
            cursor = conexion.obtener_cursor()
            sql = "DELETE FROM Pedido WHERE id = %s"
            valor = (self.id,)
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
