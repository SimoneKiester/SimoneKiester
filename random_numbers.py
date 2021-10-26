"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    """
    There is no input here, just the output of random integer numbers
    A for loop is used to count to whatever the constant NUM_RANDOM
        tells it to do.
    """
    print("This program prints out " + str(NUM_RANDOM) + " happy random numbers between 0 and 100")

    for i in range(NUM_RANDOM):
        my_random_number = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(str(my_random_number))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
