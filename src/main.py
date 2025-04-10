"""
main.py
=======

Este es el módulo principal de ejecución de la Tienda Virtual.

Se encarga de iniciar el programa y mantener el bucle principal
mientras el sistema esté en ejecución. Utiliza los módulos
`sistema` y `menu` para gestionar el flujo del programa y mostrar
los menús interactivos al usuario.

Módulos importados:
-------------------
- sistema : Proporciona funciones auxiliares como pausa, entrada y control de ejecución.
- menu    : Muestra y gestiona los distintos menús del sistema.

Ejemplo:
--------
Para iniciar la aplicación:

>>> python main.py

El programa seguirá ejecutándose hasta que el usuario decida salir.
"""

import sistema
import menu

######################## PROGRAMA ########################

# Bucle principal del programa. Se ejecuta mientras el sistema esté activo.
while sistema.en_ejecucion:
    menu.mostrar_menu(menu.titulo_predeterminado, menu.contenido_predeterminado) # Muestra inicialmente el menu por defecto
