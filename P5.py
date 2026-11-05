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
    
    if errorcode != 0:
        return (errorcode, "")

    return (errorcode, alias)
