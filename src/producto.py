"""
producto.py
===========

Este módulo define la clase `Producto`, que representa un artículo físico disponible para la venta.
Incluye propiedades como identificador, nombre, precio y stock disponible, y permite actualizar el inventario.

Clases:
-------
- Producto: Representa un producto físico estándar.

Ejemplo de uso:
---------------
>>> p = Producto("P001", "Camiseta", 19.99, 100)
>>> print(p)
 ~ ID: P001  -  Nombre: Camiseta  -  Precio: 19.99€  -  Stock: 100
"""

class Producto:
    """
    Clase que representa un producto físico con identificador, nombre, precio y stock.

    Parámetros:
    -----------
    id_producto : str
        Identificador único del producto.
    nombre_producto : str
        Nombre del producto.
    precio_producto : float
        Precio del producto en euros.
    stock_producto : int
        Cantidad disponible en inventario.

    Métodos:
    --------
    actualizar_stock(cantidad: int) -> str:
        Actualiza el stock sumando o restando unidades.
    __str__() -> str:
        Devuelve una representación legible del producto.
    """

    def __init__(self, id_producto: str, nombre_producto: str, precio_producto: float, stock_producto: int):
        self.__id_producto = id_producto
        self.__nombre_producto = nombre_producto
        self.__precio_producto = precio_producto
        self.__stock_producto = stock_producto

    @property
    def id_producto(self):
        """Obtiene o establece el ID del producto."""
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, valor):
        self.__id_producto = valor

    @property
    def nombre_producto(self):
        """Obtiene o establece el nombre del producto."""
        return self.__nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, valor):
        self.__nombre_producto = valor

    @property
    def precio_producto(self):
        """Obtiene o establece el precio del producto."""
        return self.__precio_producto

    @precio_producto.setter
    def precio_producto(self, valor):
        self.__precio_producto = valor

    @property
    def stock_producto(self):
        """Obtiene o establece el stock del producto."""
        return self.__stock_producto

    @stock_producto.setter
    def stock_producto(self, valor):
        self.__stock_producto = valor

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.

        Retorna:
        --------
        str:
            Cadena con todos los atributos del producto.
        """
        return f" ~ ID: {self.id_producto}  -  Nombre: {self.nombre_producto}  -  Precio: {self.precio_producto:0.2f}€  -  Stock: {self.stock_producto}"
    
    def actualizar_stock(self, cantidad: int):
        """
        Actualiza el stock del producto sumando o restando una cantidad.

        Parámetros:
        -----------
        cantidad : int
            Cantidad a modificar en el inventario. Puede ser negativa.

        Retorna:
        --------
        str:
            Mensaje indicando si el stock fue actualizado correctamente o si hubo un error.
        """
        if self.__stock_producto + cantidad >= 0:
            self.__stock_producto += cantidad
            return "Stock actualizado correctamente."
        else:
            return "Error! No puede haber Stock inferior a 0."
