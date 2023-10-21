import mysql.connector
from conexion import Conexion

class Categoria:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def registrarCategoria(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Solicitar al usuario el nombre de la nueva categoría
            

            sql = """
            INSERT INTO Categoria (nombre)
            VALUES (%s)
            """

            # Valores a insertar como tupla
            valores = (self.nombre,)

            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.conexion.commit()

            print(f"Categoría '{self.nombre}' insertada en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al insertar categoría en la base de datos: {error}")

    def eliminarCategoria(self, conection):
        try:
            cursor = conection.obtener_cursor()

            # Solicitar al usuario el ID de la categoría a eliminar
            categoria_id = input("Ingrese el ID de la categoría que desea eliminar: ")

            sql = "DELETE FROM Categoria WHERE id = %s"

            # Valor a insertar (el ID de la categoría a eliminar)
            valor = (categoria_id,)

            cursor.execute(sql, valor)

            # Confirma los cambios en la base de datos
            conection.commit()

            print(f"Categoría con ID {categoria_id} eliminada de la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al eliminar categoría de la base de datos: {error}")

    def actualizarCategoria(self, conexion):
        try:
            cursor = conexion.obtener_cursor()

            # Solicitar al usuario el ID de la categoría a actualizar
            categoria_id = input("Ingrese el ID de la categoría que desea actualizar: ")

            # Verificar si la categoría con el ID proporcionado existe en la base de datos
            cursor.execute("SELECT id, nombre FROM Categoria WHERE id = %s", (categoria_id,))
            categoria = cursor.fetchone()

            if not categoria:
                print(f"No se encontró ninguna categoría con el ID {categoria_id}.")
                return

            nuevo_nombre = input(f"Ingrese el nuevo nombre para la categoría (deje en blanco para mantener '{categoria[1]}'): ")

            if not nuevo_nombre:
                nuevo_nombre = categoria[1]

            sql = """
            UPDATE Categoria
            SET nombre = %s
            WHERE id = %s
            """

            # Valores a actualizar
            valores = (nuevo_nombre, categoria_id)

            cursor.execute(sql, valores)

            # Confirma los cambios en la base de datos
            conexion.commit()

            print(f"Categoría con ID {categoria_id} actualizada en la base de datos")

        except mysql.connector.Error as error:
            print(f"Error al actualizar categoría en la base de datos: {error}")

    def mostrarCategoria(self):
        # Muestra la información de la categoría.
        print(f"ID de Categoría: {self.id}")
        print(f"Nombre de Categoría: {self.nombre}")

    def mostrar_todas_las_categorias(self, conexion):
        cursor = conexion.obtener_cursor()
        sql = "SELECT * FROM Categoria"
        cursor.execute(sql)
        categorias = cursor.fetchall()

        if categorias:
            for categoria_data in categorias:
                categoria = Categoria(*categoria_data)
                categoria.mostrarCategoria()
        else:
            print("No hay categorías en la base de datos")

    def menu_categorias(self, conexion):
        pass
        """while True:
            print("\nGestionar Categorías:")
            print("1. Registrar Categoría")
            print("2. Actualizar Categoría")
            print("3. Eliminar Categoría")
            print("4. Mostrar Todas las Categorías")
            print("5. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrarCategoria(conexion)
            elif opcion == "2":
                self.actualizarCategoria(conexion)
            elif opcion == "3":
                self.eliminarCategoria(conexion)
            elif opcion == "4":
                self.mostrar_todas_las_categorias(conexion)
            elif opcion == "5":
                break"""