"""Este módulo ejecuta el programa FizzBuzz sin usar condicionales."""

from Fizz_Buzz_sinIf import fizzbuzz as fb

def main():
    """Ejecuta FizzBuzz en el rango de 1 a 50 e imprime los resultados."""
    for num in range(1, 50):
        print(num, fb(num))

if __name__ == "__main__":
    main()
