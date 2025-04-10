"""
sistema.py
==========

Este módulo proporciona funciones utilitarias para la gestión del sistema de consola e interacción con el usuario.

Funciones incluidas:
--------------------
- pause(valor)
- limpiar_consola()
- terminar_programa()
- entrada_cadena(nombre)
- entrada_numerica(nombre, tipo)
- obtener_id(f_id, listado)

Variables globales:
-------------------
- en_ejecucion : bool
    Indica si el sistema debe continuar en ejecución.

Ejemplo de uso:
---------------
>>> nombre = entrada_cadena("Nombre del producto")
>>> cantidad = entrada_numerica("Cantidad", "int")
>>> pause("continuar")
"""

import os

en_ejecucion = True
"""Variable de control que indica si el programa sigue en ejecución."""


def pause(valor: str):
    """
    Pausa la ejecución del programa hasta que el usuario pulse ENTER.

    Parámetros:
    -----------
    valor : str
        Texto a mostrar indicando la acción a realizar tras la pausa.
    """
    input(f"\n« Pulse ENTER para {valor} » ")


def limpiar_consola():
    """
    Limpia la consola del sistema operativo.
    """
    os.system("clear")


def terminar_programa():
    """
    Limpia la consola y finaliza la ejecución del programa 
    cambiando el valor de `en_ejecucion` a False.
    """
    limpiar_consola()
    global en_ejecucion
    en_ejecucion = False


def entrada_cadena(nombre: str) -> str:
    """
    Solicita al usuario una cadena de texto no vacía.

    Parámetros:
    -----------
    nombre : str
        Nombre del campo a solicitar (se usará como etiqueta).

    Retorna:
    --------
    str:
        Cadena introducida por el usuario en mayúsculas.
    """
    while True:
        cadena = input(f"{nombre.title()}: ")

        if cadena == "":
            print(f"'{nombre.upper()}' no puede estar vacío.")
            pause("reintentarlo")
        else:
            break

    return cadena.upper()


def entrada_numerica(nombre: str, tipo: str) -> int | float:
    """
    Solicita al usuario un valor numérico (entero o flotante).

    Parámetros:
    -----------
    nombre : str
        Etiqueta del campo.
    tipo : str
        Tipo de número esperado: "int" o "float".

    Retorna:
    --------
    int | float:
        Número ingresado por el usuario, según el tipo especificado.
    """
    while True:
        if tipo == "int":
            try:
                numero = int(input(f"{nombre.title()}: "))
                break
            except:
                print("Error! Solo se admiten números y no puede estar vacío.")
                pause("reintentarlo")
        else:
            try:
                numero = float(input(f"{nombre.title()}: "))
                break
            except:
                print("Error! Solo se admiten números y no puede estar vacío.")
                pause("reintentarlo")

    return numero


def obtener_id(f_id: str, listado: list | dict) -> str:
    """
    Genera un nuevo ID basado en el último ID registrado de una lista o diccionario.

    Parámetros:
    -----------
    f_id : str
        Prefijo del ID (por ejemplo, "P" para productos, "C" para clientes).
    listado : list | dict
        Colección actual de objetos o claves con IDs.

    Retorna:
    --------
    str:
        Nuevo ID generado con formato `{f_id}XXXX`.
    """
    id = ""

    if len(listado) == 0:
        id = f"{f_id}0000"

    elif isinstance(listado, list):
        id = int(listado[-1].id_producto[-4:]) + 1
        id = f"{f_id}{id:04d}"

    else:
        id = int(list(listado.keys())[-1][-4:]) + 1
        id = f"{f_id}{id:04d}"

    return id
