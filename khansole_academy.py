"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
REQUESTED_PASSES = 3


def main():
    """
    This program asks as many questions as is takes to get three
    correct answers in a row to addition problems.
    The numbers to add are two digit numbers.

    There is a way out of this, give 0 as an answer. But
        you will be called out.
    """

    right_answers = 0

    print("This is your challenge.")
    print("You have to answer three correct answers in a row to get out of this.")
    print('Or you answer "0", that is your bailout.')

    while right_answers < REQUESTED_PASSES:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        answer = int(input("What is " + str(num1) + " + " + str(num2) + "?    "))
        right_sum = num1 + num2

        # Every answer brings us closer to get out of this exercise
        if answer == right_sum:
            right_answers += 1
            print("Correct! You have gotten " + str(right_answers) + " in a row.")
        # If even one answer is wrong, the counter starts again
        if answer != right_sum:
            right_answers = 0
            print("Incorrect. The correct answer is " + str(right_sum))
        # This is my secret bailout
        if answer == 0:
            right_answers = 53

    if right_answers == 53:
        print("At least you made it out of this program")

    if right_answers == 3:
        print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
