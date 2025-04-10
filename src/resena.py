"""
resena.py
=========

Este módulo define la clase `Resena`, que representa una reseña hecha por un cliente sobre un producto específico.

Hereda atributos de las clases `Producto` y `Cliente`, y añade campos como comentario y puntuación.

Clases:
-------
- Resena: Representa la valoración de un producto realizada por un cliente.

Ejemplo de uso:
---------------
>>> r = Resena("R001", producto, cliente, "Muy buena calidad", 5)
>>> print(r)
 - ID Reseña: R001 
 - ID Producto: P001 
 - Producto: Camiseta 
 - ID Cliente : C001 
 - Cliente: Juan Pérez 
 - Comentario : Muy buena calidad 
 - Puntuación (1-5): 5
"""

from producto import Producto
from cliente import Cliente

class Resena(Producto, Cliente):
    """
    Clase que representa una reseña realizada por un cliente sobre un producto.

    Hereda de:
    ----------
    Producto, Cliente

    Parámetros:
    -----------
    id_resena : str
        Identificador único de la reseña.
    producto : object
        Instancia de la clase Producto relacionada con la reseña.
    cliente : object
        Instancia de la clase Cliente que realiza la reseña.
    comentario : str
        Comentario textual del cliente sobre el producto.
    puntuacion : int
        Valoración numérica del producto (entre 1 y 5).

    Métodos:
    --------
    __str__() -> str:
        Devuelve una representación en cadena con los detalles de la reseña.
    """

    def __init__(self, id_resena: str, producto: object, cliente: object, comentario: str, puntuacion: int):
        Producto.__init__(self, producto.id_producto, producto.nombre_producto, producto.precio_producto, producto.stock_producto)
        Cliente.__init__(self, cliente.id_cliente, cliente.nombre_cliente, cliente.email_cliente, cliente.direccion_cliente)
        self.__id_resena = id_resena
        self.__comentario = comentario
        self.__puntuacion = puntuacion

    @property
    def id_resena(self):
        """Obtiene o establece el ID de la reseña."""
        return self.__id_resena

    @id_resena.setter
    def id_resena(self, value):
        self.__id_resena = value

    @property
    def comentario(self):
        """Obtiene o establece el comentario de la reseña."""
        return self.__comentario

    @comentario.setter
    def comentario(self, value):
        self.__comentario = value

    @property
    def puntuacion(self):
        """Obtiene o establece la puntuación del producto (1 a 5)."""
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, value):
        self.__puntuacion = value

    def __str__(self):
        """
        Devuelve una representación legible de la reseña, incluyendo información del producto y del cliente.

        Retorna:
        --------
        str:
            Cadena con todos los atributos de la reseña.
        """
        return (f" - ID Reseña: {self.id_resena} \n"
                f" - ID Producto: {self.id_producto} \n"
                f" - Producto: {self.nombre_producto} \n"
                f" - ID Cliente : {self.id_cliente} \n"
                f" - Cliente: {self.nombre_cliente} \n"
                f" - Comentario : {self.comentario} \n"
                f" - Puntuación (1-5): {self.puntuacion}")
