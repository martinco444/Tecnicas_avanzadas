"""
Este módulo proporciona funciones utilitarias para la clasificación de números.
"""

import math

def es_primo(n):
    """
    Determina si un número es primo.

    Args:
        n (int): El número a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
