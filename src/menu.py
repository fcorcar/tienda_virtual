"""
menu.py
=======

Este módulo gestiona la navegación de menús dentro de la Tienda Virtual.

Define la estructura de los menús principales y secundarios, así como la lógica
para mostrar las opciones disponibles al usuario y redirigir el flujo del programa
según las selecciones realizadas.

Módulos importados:
-------------------
- funciones_menu : Contiene funciones de gestión como limpiar consola, agregar productos, clientes, etc.

Variables:
----------
- menu_principal : dict - Menú principal de navegación.
- menu_gestionar_productos : dict - Opciones para la gestión de productos.
- menu_gestionar_clientes : dict - Opciones para la gestión de clientes.
- menu_gestionar_pedidos : dict - Opciones para la gestión de pedidos.
- menu_gestionar_resenas : dict - Opciones para la gestión de reseñas.
- titulo_predeterminado : str - Título actual del menú.
- contenido_predeterminado : dict - Contenido actual del menú.

Funciones:
----------
- mostrar_titulo(titulo:str) :
    Muestra el título del menú actual en consola.

- mostrar_menu(titulo:str, contenido:dict) :
    Presenta el menú con base en el título y las opciones proporcionadas.
    Gestiona la lógica de selección de opciones y navegación entre submenús.

Ejemplo:
--------
>>> mostrar_menu(titulo_predeterminado, contenido_predeterminado)
"""

from funciones_menu import *

# ---------------------- VARIABLES ----------------------
menu_principal = {
    "1": "Gestionar Productos",
    "2": "Gestionar Clientes",
    "3": "Gestionar Pedidos",
    "4": "Gestionar Reseñas",
    "5": "Salir"
}

menu_gestionar_productos = {
    "1": "Añadir Productos",
    "2": "Listar Productos",
    "3": "Actualizar Stock",
    "4": "Volver"
}

menu_gestionar_clientes = {
    "1": "Añadir Clientes",
    "2": "Listar Clientes",
    "3": "Volver"
}

menu_gestionar_pedidos = {
    "1": "Crear Pedidos",
    "2": "Listar Pedidos",
    "3": "Calcular Total",
    "4": "Volver"
}

menu_gestionar_resenas = {
    "1": "Añadir Reseña",
    "2": "Listar Reseñas",
    "3": "Volver"
}

titulo_predeterminado = "menú principal"
contenido_predeterminado = menu_principal

# ---------------------- FUNCIONES ----------------------
def mostrar_titulo(titulo: str):
    """
    Imprime el título del menú en consola con formato en mayúsculas.

    Parámetros:
    -----------
    titulo : str
        El título a mostrar.
    """
    print(f"*** {titulo.upper()} ***")
    print()

def mostrar_menu(titulo: str, contenido: dict):     
    """
    Muestra el menú actual y gestiona la navegación y ejecución de acciones.

    Parámetros:
    -----------
    titulo : str
        El título del menú actual.
    contenido : dict
        Un diccionario con las opciones del menú.

    Nota:
    -----
    Esta función modifica las variables globales `titulo_predeterminado` y
    `contenido_predeterminado` según la navegación del usuario.
    """
    global titulo_predeterminado, contenido_predeterminado
    limpiar_consola()

    mostrar_titulo(titulo)
    for indice, apartado in contenido.items():
        print(f"  {indice}. {apartado}")

    opcion = input("\n» ")
    limpiar_consola()

    try:
        mostrar_titulo(contenido[opcion])
    except:
        pass

    match titulo:
        case "menú principal":
            match opcion:
                case "1":
                    titulo_predeterminado = "gestionar productos"
                    contenido_predeterminado = menu_gestionar_productos
                case "2":
                    titulo_predeterminado = "gestionar clientes"
                    contenido_predeterminado = menu_gestionar_clientes
                case "3":
                    titulo_predeterminado = "gestionar pedidos"
                    contenido_predeterminado = menu_gestionar_pedidos
                case "4":
                    titulo_predeterminado = "gestionar reseñas"
                    contenido_predeterminado = menu_gestionar_resenas
                case "5":
                    terminar_programa()
        
        case "gestionar productos":
            match opcion:
                case "1": agregar_productos()
                case "2": listar_productos()
                case "3": actualizar_stock()
                case "4":
                    titulo_predeterminado = "menú principal"
                    contenido_predeterminado = menu_principal

        case "gestionar clientes":
            match opcion:
                case "1": agregar_clientes()
                case "2": listar_clientes()
                case "3":
                    titulo_predeterminado = "menú principal"
                    contenido_predeterminado = menu_principal

        case "gestionar pedidos":
            match opcion:
                case "1": crear_pedido()
                case "2": listar_pedido()
                case "3": calcular_total_pedido()
                case "4":
                    titulo_predeterminado = "menú principal"
                    contenido_predeterminado = menu_principal

        case "gestionar reseñas":
            match opcion:
                case "1": agregar_resena()
                case "2": listar_resenas()
                case "3":
                    titulo_predeterminado = "menú principal"
                    contenido_predeterminado = menu_principal
