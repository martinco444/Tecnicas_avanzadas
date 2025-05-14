"""
Este módulo define la clase PrimoPerfecto para clasificar números primos perfectos.
"""

from tipo_numero import TipoNumero
from utilidades import es_primo

class PrimoPerfecto(TipoNumero):
    """
    Clase para evaluar y generar la salida de números primos perfectos.
    """
    def evaluar(self, num):
        return es_primo(num) and num < 10

    def salida(self, num):
        return f"{num} 1"
