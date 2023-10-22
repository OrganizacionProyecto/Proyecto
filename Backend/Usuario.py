import mysql.connector

class Usuario:
    def __init__(self, id, nombre, apellido, correo, contrasenia, domicilio, tipo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = contrasenia
        self.domicilio = domicilio
        self.tipo = tipo

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_contrasenia(self):
        return self.contrasenia

    def set_contrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def get_domicilio(self):
        return self.domicilio

    def set_domicilio(self, domicilio):
        self.domicilio = domicilio

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def cambiarContrasenia(self, nueva_contrasenia):
        self.contrasenia = nueva_contrasenia

    def iniciarSesion(self, correo, contrasenia):
        # Implementación para iniciar sesión de un cliente
        if self.correo == correo and self.contrasenia == contrasenia:
            return True
        else:
            return False

    def registrarUsuario(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para insertar un cliente en la base de datos
            sql = """
            INSERT INTO Usuario (id, nombre, apellido, correo, contrasenia, domicilio, tipo)
            VALUES (%s, %s, %s, %s, %s, %s,%s)
            """

            # Valores a insertar
            valores = (self.id, self.nombre, self.apellido, self.correo, self.contrasenia, self.domicilio, self.tipo)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Obtiene el ID generado para el usuario
            self.id = cursor.lastrowid

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Usuario insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar cliente en la base de datos: {error}")

    def actualizarUsuario(self, conexion, nuevo_nombre, nuevo_apellido, nuevo_correo, nueva_contrasenia, nuevo_domicilio, nuevo_tipo):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para actualizar un usuario en la base de datos
            sql = """
            UPDATE Usuario
            SET nombre = %s, apellido = %s, correo = %s, contrasenia = %s, domicilio = %s, tipo = %s
            WHERE id = %s
            """

            # Valores a actualizar
            valores = (nuevo_nombre, nuevo_apellido, nuevo_correo, nueva_contrasenia, nuevo_domicilio, nuevo_tipo, self.id)

            # Ejecuta la sentencia SQL para actualizar el usuario
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print(f"Usuario ID {self.id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar usuario en la base de datos: {error}")

    def eliminarUsuario(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Usuario WHERE id = %s"

            # Valor a insertar (el ID del usuario a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print("Eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar de la base de datos: {error}")

    def mostrarUsuario(self):
        return f"{self.nombre} {self.apellido}"


