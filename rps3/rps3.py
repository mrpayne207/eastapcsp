from random import choice, seed
seed(1)

def main():
    # get number of rounds, store in variable
    n = get_odd("How many rounds do you want to play? ", "Make sure it is a positive odd integer")

    # initialize player 1 and 2 scores to 0
    p1score = p2score = 0

    # set up a blank list to track results
    rounds = []

    # start at round 0
    round = 0

    # repeatedly play the game while no score is more than 1/2 the rounds
    while (p1score < n/2 and p2score < n/2):

        # print the round number
        print(f"---\nRound {round + 1}")

        # print the current score
        print(f"Player 1 Score: {p1score}, Computer Score: {p2score}")

        # get rps from player
        player1 = get_rps("Player 1: ", "Make sure to enter r for rock, p for paper and s for scissors").lower().strip()

        # generate a computer play and print computer play
        player2 = computer_play()
        print(f"Computer: {player2}")

        # determine winner of round
        winner = who_won(player1, player2)

        # if winner is 1, increment p1 score, add "Player 1 wins the round" to the rounds list and increment the round
        # if winner is 1, increment p2 score, add "Computer wins the round" to the rounds list and increment the round
        # else pass
        # FINISH

    # print the final score
    print(f"---\nFinal Score: Player 1: {p1score}, Computer: {p2score}")

    # if p1score > p2 score, say player 1 wins the game, else say computer wins the game
    if p1score > p2score:
        print("Player 1 Wins the game\n---")
    else:
        print("Computer Wins the game\n---")

    # print detailed results of the game
    print_results(rounds)

# validate getting an odd positive integer
def get_odd(prompt, error_message):
    # FINISH

# validate getting only r, p or s input
def get_rps(prompt, error_message):
    # FINISH

# print "Detailed Game Results:"
# then traverse list, print values of list, preceded by Round #, one value on each line
def print_results(list):
    # FINISH

# generate a random computer play of r, p or s
def computer_play():
    # FINISH

# determine who won the round based on rules of rock-paper-scissiors
# if tie, return 0, if p1 wins, return 1, if computer wins, return 2
def who_won(p1, p2):
    # FINISH

# call the main function
main()
