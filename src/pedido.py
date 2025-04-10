"""
pedido.py
=========

Este módulo define la clase `Pedido`, que representa una transacción de compra realizada por un cliente.

La clase gestiona información como el cliente asociado, los productos añadidos al pedido,
la fecha de creación y el cálculo del total del pedido.

Clases:
-------
- Pedido: Representa un pedido realizado por un cliente.

Ejemplo de uso:
---------------
>>> cliente = Cliente("123", "Juan Pérez")
>>> pedido = Pedido("123", cliente)
>>> pedido.agregar_productos(producto1)
>>> print(pedido.calcular_total())
"""

class Pedido:
    """
    Clase que representa un pedido realizado por un cliente en la tienda.

    Atributos:
    ----------
    id_cliente : str
        Identificador del cliente que realizó el pedido.
    cliente : object
        Objeto que representa al cliente.
    productos : list
        Lista de objetos producto añadidos al pedido.
    fecha : str
        Fecha en que se realiza el pedido (formato "dd/mm/yyyy").

    Métodos:
    --------
    agregar_productos(producto: object):
        Añade un producto al pedido.

    calcular_total() -> float:
        Calcula el total del pedido sumando los precios de los productos.

    __str__() -> str:
        Devuelve una representación en cadena del pedido.
    """

    def __init__(self, id_cliente: str, cliente: object):
        """
        Inicializa un nuevo pedido con un cliente y una fecha por defecto.

        Parámetros:
        -----------
        id_cliente : str
            Identificador del cliente.
        cliente : object
            Objeto que representa al cliente.
        """
        self.__id_cliente = id_cliente
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = "10/10/2025"

    @property
    def id_cliente(self):
        """Devuelve el ID del cliente."""
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        """Establece el ID del cliente."""
        self.__id_cliente = valor

    @property
    def cliente(self):
        """Devuelve el objeto cliente."""
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        """Establece el objeto cliente."""
        self.__cliente = valor

    @property
    def productos(self):
        """Devuelve la lista de productos del pedido."""
        return self.__productos

    @productos.setter
    def productos(self, valor):
        """Establece la lista de productos del pedido."""
        self.__productos = valor

    @property
    def fecha(self):
        """Devuelve la fecha del pedido."""
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        """Establece la fecha del pedido."""
        self.__fecha = valor

    def agregar_productos(self, producto: object):
        """
        Añade un producto al pedido.

        Parámetros:
        -----------
        producto : object
            El producto a añadir a la lista del pedido.
        """
        self.productos.append(producto)

    def calcular_total(self):
        """
        Calcula el total del pedido sumando los precios de los productos.

        Retorna:
        --------
        float:
            El total del pedido.
        """
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self):
        """
        Devuelve una representación en cadena del pedido.

        Retorna:
        --------
        str:
            Cadena con ID del cliente y fecha del pedido.
        """
        return f" - ID: {self.id_cliente} \n - Fecha: {self.fecha}"
