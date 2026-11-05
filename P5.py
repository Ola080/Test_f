import math
candies = ['Smarties', 'Mars', 'Twix']

def get_candy(n : int) -> str:
    try:
        return candies[n]
    except IndexError as e:
        print("Invalid choice", end=",")
    else:
        print("Valid choice", end=",")
    finally:
        print("Always go here", end=",")
    return "No candy"


#3.1.1
def divide_numbers(numerator, divisor) -> float:
    try:
        result = numerator / divisor
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero. Please provide a non-zero divisor.")
    return result
    
print(get_candy(3))

def find_square_root(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise ValueError("Input is not a number.")
    if x < 0:
        raise ValueError("Cannot compute square root of negative numbers.")
    return math.sqrt(x)

def create_alias() -> tuple[int, str]:
    alias = input("Enter your alias: ")
    errorcode = 0
    if not alias:
        errorcode = errorcode + 1
        print ("An alias cannot be the empty string")
        
    if alias[0].isdigit():
        errorcode = errorcode + 2
        print ("An alias cannot start with a digit")
    
    if len(alias)>8:
        errorcode = errorcode + 4
        print ("An alias cannot be longer than 8 characters")
    
    if alias.find(" ") != -1:
        errorcode = errorcode + 8
        print ("An alias cannot contain spaces")

    assert is_prime(2) == True, "Is prime test failed for 2"
assert is_prime(3) == True, "Is prime test failed for 3"
assert is_prime(17) == True, "Is prime test failed for 17"
assert is_prime(97) == True, "Is prime test failed for 97"

assert is_prime(4) == False, "Is prime test failed for 4"
assert is_prime(9) == False, "Is prime test failed for 9"
assert is_prime(49) == False, "Is prime test failed for 49"
assert is_prime(100) == False, "Is prime test failed for 100"

assert is_prime(1) == False, "Is prime test failed for 1"
assert is_prime(0) == False, "Is prime test failed for 0"
assert is_prime(-7) == False, "Is prime test failed for -7"

assert factorial(0) == 1, "Factorial test failed for 0"
assert factorial(1) == 1, "Factorial test failed for 1"
assert factorial(3) == 6, "Factorial test failed for 3"
assert factorial(5) == 120, "Factorial test failed for 5"
assert factorial(10) == 3628800, "Factorial test failed for 10"

try:
    factorial(-1)
except ValueError:
    pass
else:
    assert False, "Expected ValueError is not raised for factorial(-1)"
    
    if errorcode != 0:
        return (errorcode, "")

    return (errorcode, alias)
