"""
Este módulo define la clase SemiPrimoCuadratico para clasificar números semi-primos cuadráticos.
"""

import math
from tipo_numero import TipoNumero
from utilidades import es_primo

class SemiPrimoCuadratico(TipoNumero):
    """
    Clase para evaluar y generar la salida de números semi-primos cuadráticos.
    """
    def evaluar(self, num):
        raiz = int(math.sqrt(num))
        return raiz * raiz == num and es_primo(raiz)

    def salida(self, num):
        raiz = int(math.sqrt(num))
        return f"{num} 2 {raiz}"
        