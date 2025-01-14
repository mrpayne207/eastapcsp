# student name
# hangman.py

import random
random.seed()

def main():
    # generate a random word and print a definition of the word
    word = get_word_and_def()
    # determine the length of the word
    n = len(word)

    # generate a blank list for guesses guesses
    letter_guess_list = []

    # populate an letter_guess_list with "_" for all letters, else blank space " "

    # TODO

    # print blank word guess
    print_list(letter_guess_list)

    # call play game procedure, passing in word and blank guess list
    play_game(word, letter_guess_list)

def play_game(word, letter_guess_list):
    # determine length of word
    n = len(word)

    #set wrong guess count to 6
    wrong_guesses_remain = 6

    #play game while guesses remain and full word has not been guessed
    # TODO
        # call get_char procedure to get a character guess from the user, store in variable letter
        l# TODO

        # determine if letter is in word / phrase
        # TODO

            # check if letter is already in letter_check_list
            # if it is, tell player "You aready guessed {letter}, pick a new letter"
            # TODO

            # if letter is in word, traverse word to find where
            # and put letter in letter_guess_list where it goes
            # TODO


        # if letter not in list, decriment guesses and print appropariate message
        else:
            wrong_guesses_remain -= 1
            print(f"{letter} is NOT in the word, {wrong_guesses_remain} wrong guesses remaining")

        #print current status of word guess
        print_list(letter_guess_list)

    #after playing game, print win or loose message
    if "".join(letter_guess_list) == word:
        print("CONGRATULATIONS, YOU WIN!")
    else:
        print("YOU LOOSE, GAME OVER")

# traverse a list, printing east element in same line with " " after each element, then enter down after printing entire list
def print_list(list):
    # TODO

# validate getting only a single alphabetical character and return lowercase letter
def get_char(prompt, error_message):
    # TODO

    

# generate a random vocab word and print definition
def get_word_and_def():
   # list of words
    word_list = ["data abstraction"]

    # list of definitions
    definition_list = [
    "manage complexity in programs by giving a collection of data a name without referencing the specific details of the representation.",
    ]

    index = random.randint(0, len(word_list)-1)
    print(definition_list[index])
    word = word_list[index]
    return(word)

main()
