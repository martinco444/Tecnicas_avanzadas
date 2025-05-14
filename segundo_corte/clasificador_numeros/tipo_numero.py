"""
Este módulo define la clase abstracta TipoNumero para clasificar diferentes tipos de números.
"""

from abc import ABC, abstractmethod

class TipoNumero(ABC):
    """
    Clase abstracta para definir la estructura de los tipos de números.
    """
    @abstractmethod
    def evaluar(self, num: int) -> bool:
        """
        Evalúa si un número cumple con las características del tipo.

        Args:
            num (int): El número a evaluar.

        Returns:
            bool: True si el número cumple con las características, False en caso contrario.
        """
        # Método abstracto, no necesita implementación

    @abstractmethod
    def salida(self, num: int) -> str:
        """
        Genera la salida correspondiente al tipo de número.

        Args:
            num (int): El número para el cual se genera la salida.

        Returns:
            str: La salida correspondiente al tipo de número.
        """
        # Método abstracto, no necesita implementación
    