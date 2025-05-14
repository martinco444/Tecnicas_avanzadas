"""
Este módulo define la clase NumeroComun para clasificar números comunes.
"""
from tipo_numero import TipoNumero

class NumeroComun(TipoNumero):
    """
    Clase para evaluar y generar la salida de números comunes.
    """
    def evaluar(self, num):
        return True

    def salida(self, num):
        return f"{num} 0"
        