# student name
# quiz.py

# import random library
import random

def main():
    # validate getting a positive integer of states and capitals to quiz from the user
    # TODO

    # get a list of states and their capitals
    quiz_states, quiz_caps = states_and_caps(num)

    # play the quiz game
    quiz(quiz_states, quiz_caps)

# define a procedure quiz that takes in a list of states and a list of their capitals, and plays a quiz game
def quiz(quiz_states, quiz_caps):
    #initialize score to 0
    # TODO

    # repeatedly ask for the capital of each state
    # TODO

        # get a guess from the user, convert to title format
        # TODO

        # if the guess is correct, give the user a point and tell them they got it right
        # TODO

        # else tell them they got it wrong
        # TODO

    # after finishing the game, tell the user their score
    # TODO


def states_and_caps(num):
    # generate a list of integers of 50 integers from 0 to 49
    list = range(50)

    # pull random values from the list, without replacement
    index_list = random.sample(list, num)

    # list all states and their capitals
    all_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Hawaii", "Florida", "Georgia", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "North Carolina", "North Dakota", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    all_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Honolulu", "Tallahassee", "Atlanta", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Raleigh", "Bismarck", "Albany", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]
    
    # set up blank lists for the quiz
    quiz_states = []
    quiz_caps = []

    # get the states and their capitals based on their index values
    # TODO

    # return the list of states and their capitals to play the game
    # TODO

# validate getting an integer value
def get_int(prompt, error_message):
    # TODO

main()
