# Student Name
# dice.py

#import random library and seed randomizer
import random
random.seed()

#define main procedure
def main():
    # get input from user for number of dice to roll
    dice = get_int("Give an integer between 1 and 4, inclusive: ")

    # simulate rolling dice
    roll(dice)

# validate getting integer within specified range
def get_int(prompt):

    # TODO

# simulate rolling specified number of dice

def roll(dice):
    # initialize a roll counter variable
    # TODO

    # set the number of different possible rolls with that many dice
    # TODO

    # create blank rolls list to track the unique combination of dice sums
    # TODO

    # continue rolling dice while the length of the rolls list is less then the possible values
    # TODO

        # create variable to track the sum of the dice rolled
        # TODO

        # roll dice times (remember dice is an integer between 1 and 4, inclusive)
        # TODO

            # generate a random dice roll and add it to the sum
            # TODO


        # if that sum is not already in rolls list, add it
        # TODO


        # increment roll counter
        # TODO

    # print the total number of rolls that were needed to find all possible rolls valus
    # TODO

#call main function
main()
