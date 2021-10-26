"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

LIFT_OFF_START = 10


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """

    countdown = LIFT_OFF_START

    # Let's count down to 0 and then tell the spaceship to get going
    for i in range(LIFT_OFF_START):
        print(str(countdown))
        countdown -= 1
    print("Takeoff !!!!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
