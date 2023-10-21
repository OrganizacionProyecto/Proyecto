import pedido
import mysql.connector

class Cliente:
    def __init__(self, id, nombre, apellido, correo, dni, contrasenia, domicilio):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.dni = dni
        self.contrasenia = contrasenia
        self.domicilio = domicilio

    def registrarCliente(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Solicitar al usuario los datos del producto
            # Convierte la entrada a un valor numérico

            # Define la sentencia SQL para insertar un nuevo producto
            sql = """
            INSERT INTO cliente (nombre, apellido, correo, dni, contrasenia, domicilio)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            # Valores a insertar
            valores = (self.nombre, self.apellido, self.correo, self.dni, self.contrasenia, self.domicilio)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Producto insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar producto en la base de datos: {error}")

    def actualizarCliente(self, nombre=None, apellido=None, correo=None, domicilio=None, conexion=None):
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
            conexion.commit()

            print(f"Cliente ID {self.id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar cliente en la  base de datos: {error}")


    def eliminarCliente(self, conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Cliente WHERE id = %s"

            # Valor a insertar (el ID del cliente a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print("Cliente eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar cliente de la base de datos: {error}")

    def mostrarCliente(self):
        return f"{self.nombre} {self.apellido}"

    def realizarPedido(self, productos, cantidad):
        # Implementa la lógica para que un cliente realice un pedido.
        # Puedes crear una instancia de la clase Pedido y agregarla a la lista de pedidos del cliente.
        nuevo_pedido = pedido(self, productos, cantidad)
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

    