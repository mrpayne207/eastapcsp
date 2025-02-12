def main():
    # validate getting a positive integer list size from the user, 
    # using get_int and store in variable n
    #TODO

    # create a blank list num_list
    num_list = []

    # populate num_list with n integers
    #TODO

    # print the original list
    print(f"Round 0: {num_list}")

    # call the selection_sort procedure, pass in num_list as argument
    #TODO

# create procedure get_int that takes in prompt as a parameter and
# validates the input is an integer then returns the value
#TODO

# create procedure selection_sort that takes in a list as a parameter
def selection_sort(list):

    #get the length of the list, store in variable n
    #TODO

    # repeatedly sort the list n-1 times
    #TODO

        # declare min and location variables, set equal to first value / index in unsorted list
        
        # traverse the UNSORTED porotion of the list to find the minimum value
        # in the UNSORTED PORTION of the list AND keep track of its location
        # TODO

            # if you find a new minimum value, update the min value and location

        # if the minimum value is not the first element in the UNSORTED portion,
        # SWAP the minimum with the first value in the UNSORTED portion of the list
        #TODO

        # after each round of sorting, print the current status of the list
        print(f"Round {i + 1}: {list}")

# call the main procedure
main()
