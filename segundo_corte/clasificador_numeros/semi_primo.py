"""
Este módulo define la clase SemiPrimo para clasificar números semi-primos.
"""

import math
from tipo_numero import TipoNumero
from utilidades import es_primo

class SemiPrimo(TipoNumero):
    """
    Clase para evaluar y generar la salida de números semi-primos.
    """
    def evaluar(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if es_primo(i) and num % i == 0:
                j = num // i
                if es_primo(j) and i != j:
                    return True
        return False

    def salida(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if es_primo(i) and num % i == 0:
                j = num // i
                if es_primo(j) and i != j:
                    return f"{num} 3 {i} {j}"
        return f"{num} 3"
        