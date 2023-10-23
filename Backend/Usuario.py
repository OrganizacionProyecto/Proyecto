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

    def iniciarSesion(self, correo, contrasenia, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para buscar un usuario por correo y contraseña
            sql = "SELECT id, nombre, apellido, domicilio, tipo FROM Usuario WHERE correo = %s AND contrasenia = %s"

            # Valores a buscar (correo y contraseña)
            valores = (correo, contrasenia)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Recupera los datos del usuario si se encuentra
            usuario_data = cursor.fetchone()

            if usuario_data:
                # Si los datos existen en la base de datos, asigna los valores al objeto Usuario
                self.id, self.nombre, self.apellido, self.domicilio, self.tipo, = usuario_data
                print(f"Inicio de sesión exitoso. Bienvenido, {self.nombre} {self.apellido}!")
                return True
            else:
                print("Credenciales incorrectas. Inicio de sesión fallido.")
                return False

        except mysql.connector.Error as error:
            print(f"Error al iniciar sesión: {error}")
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

    def actualizarUsuario(self, conexion):
        try:
            cursor = conexion.obtener_cursor()
            usuario_id = input("Ingrese el ID del usuario que desea actualizar: ")

            # Verificar si el producto con el ID proporcionado existe en la base de datos
            cursor.execute("SELECT id FROM Usuario WHERE id = %s", (usuario_id,))
            producto = cursor.fetchone()

            if not producto:
                print(f"No se encontró ningún Usuario con el ID {usuario_id}.")
                return


            # Define la sentencia SQL para actualizar un cliente en la base de datos
            sql = """
            UPDATE Usuario
            SET nombre = %s, apellido = %s, correo = %s, contrasenia = %s, domicilio = %s
            WHERE id = %s
            """

            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            correo = input("Nuevo correo: ")
            contrasenia = input("Nueva contraseña: ")
            domicilio = input("Nuevo domicilio: ")
            # Valores a actualizar
            valores = (
                nombre if nombre  else self.nombre,
                apellido if apellido  else self.apellido,
                correo if correo  else self.correo,
                contrasenia if contrasenia  else self.contrasenia,
                domicilio if domicilio  else self.domicilio,
                usuario_id
            )

            # Ejecuta la sentencia SQL para actualizar el cliente
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print(f"Usuario ID {self.id} actualizado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar usuario en la  base de datos: {error}")
            
    def eliminarUsuario(self, conexion, id):
        
        try:
            cursor = conexion.obtener_cursor()
            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Usuario WHERE id = %s"

            # Valor a insertar (el ID del usuario a eliminar)
            valor = (id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Eliminado de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar de la base de datos: {error}")

    def mostrarTodosLosUsuarios(self, conexion):
            try:
                cursor = conexion.obtener_cursor()

                # Define la sentencia SQL para seleccionar todos los productos
                sql = "SELECT * FROM Usuario"
                cursor.execute(sql)
                Usuarios = cursor.fetchall()

                if not Usuarios:
                    print("No hay usuarios en la base de datos.")
                else:
                    print("Lista de usuarios:")
                    for usuario in Usuarios:
                        usuario_obj = Usuario(*usuario)
                        usuario_obj.mostrarUsuario()
                        print("\n")

            except mysql.connector.Error as error:
                print(f"Error al obtener la lista de usuarios: {error}")

    def mostrarUsuario(self):
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Correo:", self.correo)
        print("Domicilio:", self.domicilio)
        print("Tipo:", self.tipo)
        print()



