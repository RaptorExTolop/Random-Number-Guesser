import random

def main():
    intro()
    range = get_range() # range should have three numbers, two for the range and one for the number of guesses
    number_guessing(range)

def intro():
    end_line = "\n"
    intro = f"Hello there user, and welcome to the random number game!"
    simple_explanation = "The game is simple, input a range of number, eg 1 and 6, and then the no. of guesses you are allowed."
    print()