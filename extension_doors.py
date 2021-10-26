"""
File: extension_doors.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


def main():
    """
    Just testing the doors program to see what the math is
    """
    door = int(input("Choose door 1 or 2 or 3"))

    while door != 1 and door != 2 and door != 3:
        print(door)
        door = int(input("Choose door 1 or 2 or 3"))

    prize = 4

    if door == 1:
        prize = 2 + 9 // 10 * 100
        print("prize on door 1 = " + str(prize))
    elif door == 2:
        locked = prize % 2 != 0
        print("locked = " + str(locked))
        if not locked:
            prize += 6
        print("prize on door 2 = " + str(prize))
    elif door == 3:
        for i in range (door):
            prize += i
        print("prize on door 2 = " + str(prize))
    print("Thanks")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
