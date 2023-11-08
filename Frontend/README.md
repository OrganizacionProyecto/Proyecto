##                    Programador Full Stack - TSDWAD - 2023
##                            Proyecto Integrador I

# INTEGRANTES Grupo 7 - Com1:

JoaquinCamino12 - Camino Alonso Joaquin Nicolas - joaquincamino09@gmail.com [Backend] [Scrum Master]

Conichan - Figueroa Damián Nicolás - conichan139@gmail.com [Backend]

IamPurpleBoy - Nicolás Emanuel Martin - nicolas.emanuel.martin@gmail.com [Backend]

Andres-r3 - Andres Della Porta - andresdellaporta@outlook.com [Backend]

waltercamino - Camino Walter Daniel - waltercamino@hotmail.com [Frontend]

CeCogot - Cecilia Edith Cogot - ceciliacogot@gmail.com [Frontend]

xNachooox2442 - Gabriel Ignacio Bonzon - nachobonzon1@gmail.com [Frontend]

AntonellaAc - Antonella Acosta Gómez - antonellacosta_93@hotmail.com [Frontend]

sinistri - Sebastian Balestri - balestri@gmail.com [Frontend]

# Proyecto
    Este proyecto que hemos decidido hacer con el equipo se trata de una pagina web, la cual es una tienda virtual de la dietetica llamada Aymara. Este proyecto ha sido realizado con Python y MySQL en la parte backend, y Html, Css, Bootstrap y Javascript en la parte del frontend.

    La pagina contara con Landing page, contactos, productos y registro e ingreso.

    El programa contara con CRUD sobre los clientes, productos, categorias, usuario y administrador, las cuales modificaran directamente la base de datos.

# Requisitos
   - Python 3.7 o superior
   - Servidor MySQL (por ejemplo workbench)

# Instalación
    -Clona este repositorio en tu máquina local.
    -Configura tu servidor MySQL y asegúrate de que esté en ejecución.
    -Crea una base de datos en MySQL, esta debera llamarse 'aymara'.
    -Ejecuta el script SQL proporcionado en el archivo aymara.sql para crear las tablas y cargar datos de ejemplo en la base de datos.

# Uso
   - Ejecuta el programa del proyecto desde la carpeta Backend/main.py verificando bien los datos de conexion de la Base de datos.
   - Ademas de los metodos aplicados en el menu y submenus de la aplicacion, tambien puedes verificar los datos introducidos o los precargados desde tu servidor MySQL.
   -Las paginas se pueden ver e interactuar con ellas abriendolas en la carpeta Frontend.

# Casos de Uso
    Los casos de uso se pueden verificar desde el archivo Caso_de_Uso.pdf en la carpeta Backend.

Estructura del Proyecto:
# Backend
    La estructura backend del proyecto se compone de las siguientes carpetas y archivos:
    Backend:
        main.py
        Conexion.py (Metodos que realizan las conexiones con la base de datos)
        Producto.py (Metodos relacionados con productos)
        Categoria.py (Metodos relacionados con categorias)
        Cliente.py (Metodos relacionados con clientes)
        Pedido.py (Metodos relacionados con pedidos.)
        Usuario.py (Metodos relacionados con usuarios.)
        Administrador.py (Metodos relacionados con usuarios.)
        diagrama_clases.png (Diagrama de clases)
        Caso_de_Uso.pdf (Archivo de lectura donde se explican los casos de uso del programa python)

# Frontend
    La estructura frontend del proyecto se compone de las siguientes carpetas y archivos:
    Frontend:
        .vscode: 
            settings.json
        Imag_contacto: (Carpeta que contiene las imagenes de redes sociales y de contacto)
            correo.png
            Face.webp
            inst.png
            tw.png
            wsp.png
        Imag_productos: (Carpeta que contiene las imagenes de productos)
            aceite_coco.jpeg
            cafe_verde.jpeg
            garcimax.jpeg
        Logos: (Logo de la marca)
            icono1.ico
            logoAymara.png
        contacto.html (Pagina de contacto)
        index.html (Landing page)
        productos.html (Pagina de productos)
        ingresar.html (Pagina de registro e inicio de sesion)
        eventos.js
        Proyecto.code-workspace
        style.css
        fondo.jpeg
# Base de datos
        La estructura de la base de datos del proyecto se compone de las siguientes carpetas y archivos:
        BD:
            aymara.sql (Script de la base de datos)
            Bd_Aymara_Logico.png (Base de datos Logica)
            diagrama_conceptual_base_de_datos.png (Diagrama conceptual de la base de datos)

Notas de Versión
Versión 1.0
