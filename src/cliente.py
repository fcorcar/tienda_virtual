"""
cliente.py
==========

Este módulo define la clase `Cliente`, que representa a un cliente del sistema.

La clase encapsula información básica del cliente como su identificador, nombre,
correo electrónico y dirección.

Clases:
-------
- Cliente: Representa un cliente con información personal básica.

Ejemplo de uso:
---------------
>>> c = Cliente("C001", "Ana García", "ana@gmail.com", "Calle Falsa 123")
>>> print(c)
 - ID: C001  -  Nombre: Ana García  -  Email: ana@gmail.com  -  Dirección: Calle Falsa 123
"""

class Cliente:
    """
    Clase que representa a un cliente del sistema.

    Atributos:
    ----------
    id_cliente : str
        Identificador único del cliente.
    nombre_cliente : str
        Nombre completo del cliente.
    email_cliente : str
        Dirección de correo electrónico del cliente.
    direccion_cliente : str
        Dirección física del cliente.

    Métodos:
    --------
    __str__():
        Devuelve una representación en cadena del cliente.
    """

    def __init__(self, id_cliente:str, nombre_cliente:str, email_cliente:str, direccion_cliente:str):
        """
        Inicializa un objeto Cliente con los datos proporcionados.

        Parámetros:
        -----------
        id_cliente : str
            Identificador único del cliente.
        nombre_cliente : str
            Nombre completo del cliente.
        email_cliente : str
            Correo electrónico del cliente.
        direccion_cliente : str
            Dirección física del cliente.
        """
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__email_cliente = email_cliente
        self.__direccion_cliente = direccion_cliente

    @property
    def id_cliente(self):
        """str: Obtiene o establece el ID del cliente."""
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        self.__id_cliente = valor

    @property
    def nombre_cliente(self):
        """str: Obtiene o establece el nombre del cliente."""
        return self.__nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, valor):
        self.__nombre_cliente = valor

    @property
    def email_cliente(self):
        """str: Obtiene o establece el email del cliente."""
        return self.__email_cliente

    @email_cliente.setter
    def email_cliente(self, valor):
        self.__email_cliente = valor

    @property
    def direccion_cliente(self):
        """str: Obtiene o establece la dirección del cliente."""
        return self.__direccion_cliente

    @direccion_cliente.setter
    def direccion_cliente(self, valor):
        self.__direccion_cliente = valor

    def __str__(self):
        """
        Devuelve una representación legible del cliente.

        Retorna:
        --------
        str:
            Cadena con los datos del cliente.
        """
        return f" - ID: {self.id_cliente}  -  Nombre: {self.nombre_cliente}  -  Email: {self.email_cliente}  -  Dirección: {self.direccion_cliente}"
