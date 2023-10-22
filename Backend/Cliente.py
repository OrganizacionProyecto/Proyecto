import Pedido
import mysql.connector
from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasenia, domicilio, tipo, dni, id_usuario):
        super().__init__(id, nombre, apellido, correo, contrasenia, domicilio, tipo)
        self.dni = dni
        #self.pedidos = [] //para acumular el historial del cliente en otra etapa
        self.id_usuario = id_usuario

    def realizarPedido(self, productos, cantidad):
        nuevo_pedido = Pedido(self, productos, cantidad)
        self.pedidos.append(nuevo_pedido)
    
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def asignarIdUsuario(self, id):
        self.id_usuario = id
    
    def registrarCliente(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para insertar un cliente en la base de datos
            sql = """
            INSERT INTO Cliente (dni, id_usuario)
            VALUES (%s, %s)
            """

            # Valores a insertar
            valores = (self.dni, self.id_usuario)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Obtiene el ID generado para el cliente
            self.id = cursor.lastrowid

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Cliente insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar cliente en la base de datos: {error}")

    def eliminarCliente(self,conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Cliente WHERE id = %s"

            # Valor a insertar (el ID del cliente a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Cliente eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar categoria de la base de datos: {error}")
