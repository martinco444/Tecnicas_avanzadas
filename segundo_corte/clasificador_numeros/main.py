"""
Este módulo clasifica números según diferentes criterios y procesa archivos de entrada.
"""

import sys
from primo_perfecto import PrimoPerfecto
from semi_primo_cuadratico import SemiPrimoCuadratico
from semi_primo import SemiPrimo

def clasificar_codigo(n):
    """
    Clasifica un número y devuelve un código basado en su tipo.

    Args:
        n (int): El número a clasificar.

    Returns:
        int: El código correspondiente al tipo del número.
    """
    if PrimoPerfecto().evaluar(n):
        return 1
    if SemiPrimoCuadratico().evaluar(n):
        return 2
    if SemiPrimo().evaluar(n):
        return 3
    return 0

def procesar_archivo(nombre_entrada, nombre_salida):
    """
    Procesa un archivo de entrada y escribe los resultados en un archivo de salida.

    Args:
        nombre_entrada (str): Ruta del archivo de entrada.
        nombre_salida (str): Ruta del archivo de salida.
    """
    with open(nombre_entrada, 'r', encoding='utf-8') as entrada, \
         open(nombre_salida, 'w', encoding='utf-8') as salida:
        for linea in entrada:
            linea = linea.strip()
            try:
                numero = int(linea)
                codigo = clasificar_codigo(numero)
                salida.write(f"{numero} {codigo}\n")
            except ValueError:
                salida.write(f"Entrada invalida: {linea}\n")

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--archivo":
        procesar_archivo(sys.argv[2], "output.txt")
    else:
        print("Entrada inválida. Usa un número entero o '--archivo nombre.txt'")
