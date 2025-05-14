import pytest
from Fizz_Buzz_sinIf import fizzbuzz

def test_fizzbuzz_general():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    
def test_fizzbuzz_multiplos_tres():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    

def test_fizzbuzz_multiplos_cinco():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"