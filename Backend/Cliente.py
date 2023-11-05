from Pedido import Pedido
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

            # Solicitar al usuario los datos del producto
            # Convierte la entrada a un valor numérico
            
            # Define la sentencia SQL para insertar un nuevo producto
            sql = """
            INSERT INTO cliente (dni, id_usuario)
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

            print("Producto insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar producto en la base de datos: {error}")

    def eliminarCliente(self,conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para actualizar un cliente en la base de datos
            sql = """
            UPDATE Cliente
            SET nombre = %s, apellido = %s, correo = %s, domicilio = %s
            WHERE id = %s
            """

            # Valores a actualizar
            valores = (
                nombre if nombre is not None else self.nombre,
                apellido if apellido is not None else self.apellido,
                correo if correo is not None else self.correo,
                domicilio if domicilio is not None else self.domicilio,
                self.id
            )

            # Ejecuta la sentencia SQL para actualizar el cliente
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Producto insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar producto en la base de datos: {error}")

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
            print(f"Error al eliminar cliente de la base de datos: {error}")

    def mostrarCliente(self):
        return f"{self.nombre} {self.apellido}"

    def realizarPedido(self, productos, cantidad):
        # Implementa la lógica para que un cliente realice un pedido.
        # Puedes crear una instancia de la clase Pedido y agregarla a la lista de pedidos del cliente.
        nuevo_pedido = Pedido(self, productos, cantidad)
        self.pedidos.append(nuevo_pedido)

    def cambiarContrasenia(self, nueva_contrasenia):
        # Implementa la lógica para que el cliente cambie su contraseña.
        self.contrasenia = nueva_contrasenia

    def iniciarSesion(self, correo, contrasenia):
        # Implementación para iniciar sesión de un cliente
        if self.correo == correo and self.contrasenia == contrasenia:
            return True
        else:
            return False

