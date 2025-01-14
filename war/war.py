import random
random.seed()

def main():
    # set up a deck of 52 cards with VALUE-SUIT
    card_deck = ["A-C", "K-C", "Q-C", "J-C", "10-C", "9-C", "8-C", "7-C", "6-C", "5-C", "4-C", "3-C", "2-C",
                 "A-D", "K-D", "Q-D", "J-D", "10-D", "9-D", "8-D", "7-D", "6-D", "5-D", "4-D", "3-D", "2-D",
                 "A-H", "K-H", "Q-H", "J-H", "10-H", "9-H", "8-H", "7-H", "6-H", "5-H", "4-H", "3-H", "2-H",
                 "A-S", "K-S", "Q-S", "J-S", "10-S", "9-S", "8-S", "7-S", "6-S", "5-S", "4-S", "3-S", "2-S"]
    # shuffle the deck of cards 5 times
    # TODO

    #deal the deck of cards into 2 equal player sets
    deck1, deck2 = deal(card_deck)

    #set up a blank list for a "pot" in case of a war
    war_pot = []

    # set up a round counting variable
    round_count = 0

    # set up a global variable for counting the number of wars and initialize to 0
    global war_count
    war_count = 0

    # play the game while player 1 has between at least 1 cards and less than a full deck
    while len(deck1) > 0 and len(deck1) < 52:

        # shuffle decks every 10 rounds
        if round_count % 10 == 0:
            random.shuffle(deck1)
            random.shuffle(deck2)

        # play a round of war
        play_round(deck1, deck2, war_pot)

        #increment the round counter
        round_count += 1

    # print output from the results of the game once it is over
    print(f"The game took {round_count} rounds and had {war_count} wars")
    print(f"The final decks are: ")
    print(f"Player 1: {deck1}")
    print(f"Player 2: {deck2}")

# define a procedure that plays a round of war, getting 2 decks of cards and a war_pot list
def play_round(deck1, deck2, war_pot):

    # draw the first cards from each deck, remove it that cards from each deck and print the cards
    card1 = deck1[0]
    deck1.pop(0)
    card2 = deck2[0]
    deck2.pop(0)
    print(f"Player 1: {card1}, Player 2: {card2}")

    # determine the winner of the round
    winner = check_win(card1, card2)

    # if 1 is the winnder, add the cards to the end of that deck along with any cards from the war pot
    # then clear the war pot and print the restults of the round
    if winner == 1:
        deck1.append(card1)
        deck1.append(card2)
        deck1.extend(war_pot)
        war_pot.clear()
        print(f"Player 1 Wins, Player 1 has {len(deck1)} cards, Player 2 has {len(deck2)} cards.")

    # if 2 is the winnder, add the cards to the end of that deck along with any cards from the war pot
    # then clear the war pot and print the restults of the round
    elif winner == 2:
        deck2.append(card1)
        deck2.append(card2)
        deck2.extend(war_pot)
        war_pot.clear()
        print(f"Player 2 Wins, Player 1 has {len(deck1)} cards, Player 2 has {len(deck2)} cards.")

    # if no winner than it is a war
    else:
        print("WAR")
        global war_count
        #increment war_count
        war_count += 1
        # only play war if each deck has enough cards
        if (len(deck1) > 3 and len(deck2) > 3):
            # add current cards to the war pot
            war_pot.append(card1)
            war_pot.append(card2)
            # add 3 more cards from each pile to the war pot

            # TODO

            # play a new round of war
            play_round(deck1, deck2, war_pot)
        # if there are not enough cards in deck 1, give all cards to deck 2
        elif len(deck1) < 2:
            print("Player 1 does not have enough cards, Player 2 gets them all")
            deck2.append(card1)
            deck2.append(card2)
            deck2.extend(deck1)
            deck1.clear()
        # else there are not enough cards in deck 2, so give all cards to deck 1
        else:
            print("Player 2 does not have enough cards, Player 1 gets them all")
            deck1.append(card1)
            deck1.append(card2)
            deck1.extend(deck2)
            deck2.clear()

# write a procedure to deal cards
def deal(cards):

    # set up 2 blank lists, 1 for each player
    # TODO

    # give half a deck (26 cards) to each player
    # TODO
        # add first card in list to player1, add second card to player2 and remove cards from deck
        # TODO


    # print the cards that player 1 and player 2 have
    print(f"Player 1 original cards: {player1}")
    print(f"Player 2 original cards: {player2}")

    # return the decks of cards to the players
    return(player1, player2)

# define a procedure to determine who wins a round of the game
def check_win(card1, card2):
    # split cards between their value and their suit, converting values to integers
    val1, suit1 = card1.split("-")
    val1 = convert_val(val1)
    val2, suit2 = card2.split("-")
    val2 = convert_val(val2)
    if val1 > val2:
        return 1
    elif val2 > val1:
        return 2
    else:
        return 3


# converting values from strings and face cards to integers
def convert_val(val):
    if val.isdigit():
        val = int(val)
    elif val == 'A':
        val = 14
    elif val == 'K':
        val = 13
    elif val == 'Q':
        val = 12
    elif val == 'J':
        val = 11
    return val

# call the main procedure
main()
