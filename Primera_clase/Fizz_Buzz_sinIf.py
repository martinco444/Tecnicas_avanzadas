def fizzbuzz(i) -> str:
    return ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i)