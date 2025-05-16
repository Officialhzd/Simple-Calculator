from functions import tokenize, add, subtract, multiply, divide

def main():
    """
    Main function to run the calculator.
    Handles user input, tokenization, calculation, and error handling.
    """
    try:
        # Prompt user for input and remove leading/trailing whitespace
        user_input = input("Calculate: ").strip()
        if not user_input:
            print("No input provided.")
            return

        # Tokenize the input expression into numbers and operators
        token = tokenize(user_input)
        if not token or len(token) < 3:
            print("Invalid expression. Please enter a valid calculation (e.g., 2+3*4).")
            return

        result = token[0]

        # Iterate through the tokens and perform calculations
        for i in range(1, len(token), 2):
            operator = token[i]
            try:
                next_num = token[i + 1]
            except IndexError:
                # Handles cases where the expression ends with an operator
                print("Incomplete expression. Please check your input.")
                return

            # Perform the operation based on the operator
            match operator:
                case "+":
                    result = add(result, next_num)
                case "-":
                    result = subtract(result, next_num)
                case "*":
                    result = multiply(result, next_num)
                case "/":
                    try:
                        result = divide(result, next_num)
                    except ZeroDivisionError:
                        # Handle division by zero error
                        print("Error: Division by zero.")
                        return
                case _:
                    # Handle invalid operator
                    print(f"Invalid Operator '{operator}' encountered!")
                    return

        # Output the final result
        print(f"Result: {result}")

    except Exception as e:
        # Catch-all for any unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()