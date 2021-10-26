"""
File: nimm.py
-------------------------
Add your comments here.
"""
import math

STONES_TO_BEGIN_WITH = 20


def main():
    """
    This program asks two players to take turns removing either 1 or two stones from a pile.
    Whoever takes the last stone loses the game.
    The players start out with 20 stones.
    """

    stones_left = STONES_TO_BEGIN_WITH
    # player 1 would begin
    current_player = 1

    # this loop lets players remove stones until no stone is left
    while stones_left > 0:
        print("There are " + str(stones_left) + " stones left.")
        stones_to_remove = aks_for_number_of_stones_to_remove(current_player)
        stones_left = stones_left - stones_to_remove
        current_player = switch_player(current_player)

    print("Player " + str(current_player) + ", Congratulations. You won the game.")
    if stones_left == 0:
        print("Player " + str(switch_player(current_player)) + ", you took the last stone and lost")
    elif stones_left < 0:
        print("Player " + str(switch_player(current_player)) + ", you took even more stones than available and lost")
    else:
        print("something went wrong in this game, how did we end up with " + str(stones_left) + " stones?")


def switch_player(current_player):
    """
    Assuming that there are only two players, the current_player is
    switched from 1 to 2 or from 2 to 1
    Doctests:
    >>> switch_player(1)
    2
    >>> switch_player(2)
    1
    >>> switch_player(3)
    1
    """
    if current_player == 1:
        return 2
    else:
        return 1


def aks_for_number_of_stones_to_remove(current_player):
    stones_out = 0
    # ask player 1 how many stones to take out, repeat until input is one or two
    while (stones_out < 1) or (stones_out > 2):
        stones_out = int(input("Player " + str(current_player) + ", would you like to remove 1 or 2 stones?  "))
    return stones_out


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
