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

print(get_candy(3))