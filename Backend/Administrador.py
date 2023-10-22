from Usuario import Usuario
import mysql.connector

class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasenia, domicilio, tipo, id_usuario):
        super().__init__(id, nombre, apellido, correo, contrasenia, domicilio,tipo)
        self.id_usuario =id_usuario

    
    def get_id_usuario(self):
        return self.id_usuario
    
    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario
       
    def registrarAdmin(self, conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para insertar un cliente en la base de datos
            sql = """
            INSERT INTO Administrador (id_usuario)
            VALUES (%s)
            """

            # Valores a insertar
            valores = (self.id_usuario,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Obtiene el ID generado para el administrador
            self.id = cursor.lastrowid

            # Confirma los cambios en la base de datos
            conexion.commit()

            print("Admiistrador insertado en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar Administrador en la base de datos: {error}")


    def procesarPedidos(self):
        
        pass

    def gestionarProductos(self):
        
        pass

    def gestionarCategorias(self):
        
        pass


    def tipoUsuario(self):
        
        pass

