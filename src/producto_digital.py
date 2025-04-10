"""
producto_digital.py
===================

Este módulo define la clase `ProductoDigital`, una subclase de `Producto`, 
diseñada para representar productos descargables o digitales.

Extiende la funcionalidad básica del producto añadiendo propiedades específicas como 
el formato del archivo y su tamaño en gigabytes.

Clases:
-------
- ProductoDigital: Representa un producto digital como software, e-books, música, etc.

Ejemplo de uso:
---------------
>>> pd = ProductoDigital("D001", "Ebook Python", 9.99, 50, "PDF", 2.5)
>>> print(pd)
 ~ ID: D001  -  Nombre: Ebook Python  -  Precio: 9.99€  -  Stock: 50  -  Formato: PDF  -  Tamaño: 2.50GB
"""

from producto import Producto

class ProductoDigital(Producto):
    """
    Clase que representa un producto digital, como un libro electrónico o software.

    Hereda de:
    ----------
    Producto

    Atributos adicionales:
    ----------------------
    formato : str
        Formato del archivo digital (por ejemplo, PDF, MP3, EXE).
    tamano : float
        Tamaño del archivo en gigabytes (GB).

    Métodos:
    --------
    __str__():
        Devuelve una representación legible del producto digital.
    """

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        """
        Inicializa un producto digital con todos sus atributos.

        Parámetros:
        -----------
        id_producto : str
            Identificador único del producto.
        nombre : str
            Nombre del producto.
        precio : float
            Precio del producto en euros.
        stock : int
            Cantidad disponible.
        formato : str
            Formato del archivo digital.
        tamano : float
            Tamaño del archivo en GB.
        """
        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamano = tamano

    @property
    def formato(self):
        """Devuelve el formato del producto digital."""
        return self.__formato

    @formato.setter
    def formato(self, valor):
        """Establece el formato del producto digital."""
        self.__formato = valor

    @property
    def tamano(self):
        """Devuelve el tamaño del archivo del producto digital en GB."""
        return self.__tamano

    @tamano.setter
    def tamano(self, valor):
        """Establece el tamaño del archivo del producto digital en GB."""
        self.__tamano = valor

    def __str__(self):
        """
        Devuelve una representación en cadena del producto digital.

        Retorna:
        --------
        str:
            Cadena con todos los atributos del producto.
        """
        return (f" ~ ID: {self.id_producto}  -  Nombre: {self.nombre_producto}  -  Precio: {self.precio_producto:0.2f}€  "
                f" -  Stock: {self.stock_producto}  -  Formato: {self.formato}  -  Tamaño: {self.tamano:0.2f}GB")
