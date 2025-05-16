def tokenize(expression):
    """
    Converts a string mathematical expression into a list of numbers and operators.
    Only supports +, -, *, / operators and positive integers.
    Ignores invalid characters.
    """
    token = []
    number = ""

    for char in expression:
        if char.isdigit():
            number += char
        else:
            if number:
                try:
                    token.append(float(number))
                except ValueError:
                    # Handle invalid number conversion
                    pass
            number = ""
            if char in ["+", "-", "*", "/"]:
                token.append(char)
            # Ignore any other characters

    if number:
        try:
            token.append(float(number))
        except ValueError:
            pass

    return token

def add(a, b):
    """Returns the sum of a and b."""
    try:
        return a + b
    except TypeError:
        print("Error: Invalid types for addition.")
        raise

def subtract(a, b):
    """Returns the difference of a and b."""
    try:
        return a - b
    except TypeError:
        print("Error: Invalid types for subtraction.")
        raise

def multiply(a, b):
    """Returns the product of a and b."""
    try:
        return a * b
    except TypeError:
        print("Error: Invalid types for multiplication.")
        raise

def divide(a, b):
    """Returns the quotient of a and b. Raises ZeroDivisionError if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
        raise
    except TypeError:
        print("Error: Invalid types for division.")
        raise