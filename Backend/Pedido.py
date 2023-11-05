import mysql.connector
from Producto import Producto
from Usuario import Usuario

class Pedido:
    def __init__(self, id, id_usuario, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.estado = estado
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

    def enviarMail(self, conexion, id):
        cursor = conexion.obtener_cursor()

        try:
            # Define la consulta SQL para buscar el pedido por su ID
            consulta = "SELECT * FROM Pedido WHERE id = %s"
            # Ejecuta la consulta con el ID del pedido a buscar
            cursor.execute(consulta, (id,))
            # Obtiene los resultados de la consulta
            resultado = cursor.fetchone()
            print(f"Verificacion del pedido numero: {resultado[0]}")
            print(f"Estado: {resultado[2]}")
            if resultado:
                id_usuario = resultado[1]
                # Define la consulta SQL para buscar los datos de usuario que realizo el peddido
                consulta = "SELECT * FROM usuario WHERE id = %s"
                # Ejecuta la consulta con el ID del pedido a buscar
                cursor.execute(consulta, (id_usuario,))
                # Obtiene el resultado de la consulta
                resultadoUsuario = cursor.fetchone()
                
                if resultadoUsuario:
                    #Muestro la tupla con toda la informacion del usuario que realizo el pedido
                    print("A nombre de: ")
                    print(f"Nombre: {resultadoUsuario[1]}")
                    print(f"Apellido: {resultadoUsuario[2]}")
                    print(f"Correo: {resultadoUsuario[3]}")
                    print(f"Domicilio: {resultadoUsuario[5]}")
                else:
                    print(f"No se encontró ningún usuario con ID {id_usuario}")

                   
               
            else:
                print(f"No se encontró ningún pedido con ID {id}")
        except mysql.connector.Error as error:
            print(f"Error al buscar el pedido en la base de datos: {error}")   

        cursor.close()              

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
            self.enviarMail(conexion, self.id)

        except mysql.connector.Error as error:
            print(f"Error al insertar pedido en la base de datos: {error}")

    def eliminarPedido(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Obtén todos los registros de Pedido_Producto relacionados con el pedido
            sql_obtener_relaciones = "SELECT id FROM Pedido_Producto WHERE pedido_id = %s"
            cursor.execute(sql_obtener_relaciones, (self.id,))
            relaciones = cursor.fetchall()

            # Elimina los registros relacionados en Pedido_Producto
            for relacion in relaciones:
                sql_eliminar_relacion = "DELETE FROM Pedido_Producto WHERE id = %s"
                cursor.execute(sql_eliminar_relacion, (relacion[0],))

            # Ahora puedes eliminar el pedido
            sql_eliminar_pedido = "DELETE FROM Pedido WHERE id = %s"
            cursor.execute(sql_eliminar_pedido, (self.id,))

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Pedido y registros relacionados eliminados de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar pedido y registros relacionados de la base de datos: {error}")


    def obtenerProductosDelPedido(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Consultar si el usuario existe en la tabla de usuarios
            consulta = "SELECT * FROM usuarios WHERE nombre = ?;"
            cursor.execute(consulta, (self.usuario,))
            resultado = cursor.fetchone()

            # Cerrar la conexión a la base de datos
            cursor.close()

            return resultado

        except mysql.connector.Error as error:
            print(f"Error al obtener productos del pedido: {error}")
            return None

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
