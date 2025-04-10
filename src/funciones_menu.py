"""
funciones_menu.py
=================

Este módulo contiene las funciones que gestionan el flujo de interacción con el usuario
a través de menús para manipular productos, clientes, pedidos y reseñas.

Funciones principales:
----------------------
1. Gestión de productos:
   - agregar_productos()
   - listar_productos()
   - actualizar_stock()

2. Gestión de clientes:
   - agregar_clientes()
   - listar_clientes()

3. Gestión de pedidos:
   - crear_pedido()
   - listar_pedido()
   - calcular_total_pedido()

4. Gestión de reseñas:
   - agregar_resena()
   - listar_resenas()

Variables globales:
-------------------
- listado_productos : list
    Lista de instancias de Producto o ProductoDigital.
- listado_clientes : dict
    Diccionario con ID como clave e instancias de Cliente como valor.
- listado_pedidos : list
    Lista de instancias de Pedido.
- listado_resenas : list
    Lista de instancias de Reseña.
"""

############# IMPORTACIONES ##############
from sistema import *
from cliente import Cliente
from producto import Producto
from producto_digital import ProductoDigital
from pedido import Pedido


############# VARIABLES ##############
listado_productos = []
"""Lista de productos registrados (Producto y ProductoDigital)."""

listado_clientes = {}
"""Diccionario de clientes registrados."""

listado_pedidos = []
"""Lista de pedidos realizados."""

listado_resenas = []
"""Lista de reseñas registradas."""


## 1. Gestionar Productos

def agregar_productos():
    """
    Solicita datos al usuario para agregar un producto (físico o digital)
    y lo añade a `listado_productos`.
    """
    print("  1. Añadir Producto Físico")
    print("  2. Añadir Producto Digital")
    op = input("\n» ")

    match op:
        case "1":
            nombre = entrada_cadena("nombre producto")
            precio = entrada_numerica("precio", "float")
            stock = entrada_numerica("stock", "int")
            id_pro = obtener_id("P", listado_productos)
            listado_productos.append(Producto(id_pro, nombre, precio, stock))

        case "2":
            nombre = entrada_cadena("nombre producto")
            precio = entrada_numerica("precio", "float")
            stock = entrada_numerica("stock", "int")
            formato = entrada_cadena("formato")
            tamano = entrada_numerica("tamaño", "float")
            id_pro = obtener_id("PD", listado_productos)
            listado_productos.append(ProductoDigital(id_pro, nombre, precio, stock, formato, tamano))

    print("Añadido con éxito.")
    pause("volver al menú")


def listar_productos():
    """
    Muestra en pantalla todos los productos registrados en `listado_productos`.
    """
    if len(listado_productos) == 0:
        print("Aun no hay productos.")

    for producto in listado_productos:
        print(producto)

    pause("volver al menú")


def actualizar_stock():
    """
    Permite actualizar el stock de un producto existente.
    """
    nombre = entrada_cadena("nombre producto")

    for producto in listado_productos:
        if producto.nombre_producto == nombre:
            stock = entrada_numerica("stock", "int")
            print(producto.actualizar_stock(stock))
            break
    else:
        print("El producto no existe.")

    pause("volver al menú")


## 2. Gestionar Clientes

def agregar_clientes():
    """
    Solicita datos para registrar un nuevo cliente en `listado_clientes`.
    """
    nombre = entrada_cadena("nombre cliente")
    email = entrada_cadena("email")
    direccion = entrada_cadena("dirección")
    id_clie = obtener_id("C", listado_clientes)
    listado_clientes[id_clie] = Cliente(id_clie, nombre, email, direccion)

    print("Añadido con éxito.")
    pause("volver al menú")


def listar_clientes():
    """
    Muestra todos los clientes registrados en el sistema.
    """
    if len(listado_clientes) == 0:
        print("Aun no hay productos.")

    for cliente in listado_clientes.values():
        print(cliente)

    pause("volver al menú")


## 3. Gestionar Pedidos

def crear_pedido():
    """
    Crea un nuevo pedido para un cliente y permite agregarle productos.
    """
    id_clien = entrada_cadena("ID cliente")
    for i in listado_clientes.keys():
        if i == id_clien:
            listado_pedidos.append(Pedido(i, listado_clientes[i]))
            nombre = entrada_cadena("nombre producto")
            for pro in listado_productos:
                if pro.nombre_producto == nombre:
                    listado_pedidos[-1].agregar_productos(pro)
                    print("Añadido con éxito.")
                    break
            else:
                print("Error! El producto no existe.")
            break
    else:
        print("Error! El cliente no existe.")

    pause("volver al menú")


def listar_pedido():
    """
    Muestra los productos asociados a un pedido de un cliente.
    """
    id_clien = entrada_cadena("ID cliente")

    for i in listado_pedidos:
        if i.id_cliente == id_clien:
            for pro in i.productos:
                print(f" - {pro}")
            break
    else:
        print("Error! El cliente no existe")

    pause("volver al menú")


def calcular_total_pedido():
    """
    Calcula y muestra el total de un pedido para un cliente específico.
    """
    id_clien = entrada_cadena("ID cliente")

    for i in listado_pedidos:
        if i.id_cliente == id_clien:
            print(f"{i.calcular_total():0.2f}€")
            break
    else:
        print("Error! El cliente no existe")

    pause("volver al menú")


## 4. Gestionar Reseñas

def agregar_resena():
    """
    Placeholder para agregar reseñas. (Funcionalidad por implementar)
    """
    pause("volver al menú")


def listar_resenas():
    """
    Placeholder para listar reseñas. (Funcionalidad por implementar)
    """
    pause("volver al menú")
