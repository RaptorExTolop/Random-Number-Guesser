# import section
import random

#
new_line = "\n"


def main():
    name = intro()
    range = get_range(name) # range should have three numbers, two for the range and one for the number of guesses
    number_guessing(name, range)

def intro():
    intro = f"Hello there user, and welcome to the random number game!"
    simple_explanation = "The game is simple, input a range of number, eg 1 and 6, and then the no. of guesses you are allowed."
    print(intro, new_line, simple_explanation)
    name = input("May I ask what you name is? ")
    input(f"Thank you, {name}. Press any button to begin!")
    return name
