"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""
import math

def main():
    """
    Program asks the user for input of two real numbers
    It prints out the difference first number minus second number
    """
    # Introduction
    print("This program subtracts one number from another")

    # Asking the user to put in the two numbers
    num1 = float(input("Enter first number (minuend): "))
    num2 = float(input("Enter second number (subtrahend): "))

    # Printing the result num1 - num2
    print("The result (difference) is: " + str(num1 - num2))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
