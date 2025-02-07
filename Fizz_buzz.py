def fizzbuzz(i) -> str:
    if(i % 3 == 0 and i % 5 == 0):
        return "FizzBuzz"
    if (i % 3 == 0):
        return "Fizz"
    if (i % 5 == 0):
        return "Buzz"      
    return str(i)
                    
                    
            