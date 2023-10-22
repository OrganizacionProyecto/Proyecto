import mysql.connector

class Categoria:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def registrarCategoria(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            sql = """
            INSERT INTO Categoria (id, nombre)
            VALUES (%s, %s)
            """

            # Valores a insertar como tupla
            valores = (self.id, self.nombre)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Categoría insertada en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar categoría en la base de datos: {error}")

    
    def eliminarCategoria(self,conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Define la sentencia SQL para eliminar un cliente de la base de datos
            sql = "DELETE FROM Categoria WHERE id = %s"

            # Valor a insertar (el ID del cliente a eliminar)
            valor = (self.id,)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print("Categoria eliminada de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar categoria de la base de datos: {error}")

    def actualizarCategoria(self, nombre, conexion):
        try:
            cursor = conexion.cursor()

            # Define la sentencia SQL para actualizar una categoría en la base de datos
            sql = """
            UPDATE Categoria
            SET nombre = %s
            WHERE id = %s
            """

            # Valores a actualizar
            valores = (nombre, self.id)

            # Ejecuta la sentencia SQL
            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print(f"Categoría ID {self.id} actualizada en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar categoría en la base de datos: {error}")

    def mostrarCategoria(self):
        # Muestra la información de la categoría.
        print(f"ID de Categoría: {self.id}")
        print(f"Nombre de Categoría: {self.nombre}")

    def productosCategoria(self):
        pass

