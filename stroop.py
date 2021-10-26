import time
import random
from termcolor import colored

PHASE_TIME_S = 10

def main():
    # print_intro()
    # Your solution goes here
    easy = quiz_user_clear_messages()
    difficult = quiz_user_mixed_messages()
    if easy > difficult:
        print("You scored " + str(easy-difficult) + " times less, when distracted.")
    elif easy == difficult:
        print("Wow, distraction does not seem to make a difference")
    else:
        print("It seems, distraction is good for you. You scored " + str(difficult - easy) + " times more, when distracted.")


def quiz_user_clear_messages():
    print("Let's try easy.")
    time1 = time.time()
    tally = 0
    while time.time() < time1 + PHASE_TIME_S:
        color = random_color_name()
        print_in_color(color, color)
        newcolor = input("What is the color of this text? - ")
        if newcolor == color:
            tally += 1
    print ("You scored: " + str(tally))
    return tally
    
def quiz_user_mixed_messages():
    print("This is more complicated, focus!")
    time1 = time.time()
    tally = 0
    while time.time() < time1 + PHASE_TIME_S:
        color_name = random_color_name()
        color_tint = random_color_name()
        
        print_in_color(color_name, color_tint)
        newcolor = input("What is the color of this text? - ")
        if newcolor == color_tint:
            tally += 1
    print ("You scored: " + str(tally))
    return tally

# We were cut off - thanks, Jonathan!
def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('purple', 'purple')

def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'purple'])

def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'purple': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()
