import mysql.connector

class Conexion:
    def __init__(self, host, usuario, contrasenia, base_datos):
        self.host = host
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.base_datos = base_datos
        self.conexion = None

    def conectar(self):
        try:
            # Configura la conexión a la base de datos
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.contrasenia,
                database=self.base_datos
            )

            # Verifica si la conexión fue exitosa
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")

        except mysql.connector.Error as error:
            print(f"Error de MySQL: {error}")

    def cerrar(self):
        # Cierra la conexión cuando hayas terminado de usarla
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    def obtener_cursor(self):
        # Devuelve un cursor para la conexión actual
        if self.conexion is not None and self.conexion.is_connected():
            return self.conexion.cursor()
        else:
            print("Error: La conexión a la base de datos no está establecida.")

            return None

