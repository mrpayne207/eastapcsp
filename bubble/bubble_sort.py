# get a list of integers from the user, use the bubble sort algorithm to sort the list from smallest to largest

def main():
    # get a positive list size from the user, store in variable n


    # create a blank list num_list



    # populate num_list with n integers



    # print the original list
    print(f"Round 0: {num_list}")


    # call the bubble_sort porcedure, pass in num_list as an argument
    bubble_sort(num_list)


# create a procedure that validates the input is an integer


# create a porcedure that implements bubble_sort that takes in a list and uses the bubble sort algorithm
def bubble_sort(list):

    # get the length of the list, store in variable n



    # traverse every element except for the last element


        # traverse the unsoreted list each time (from 0 to n - i - 1)


            # if the current elemement (j) is less bigger than the next element (j+1), swap them


        # print the status of the list after each round through the list
        print(f"Round {i + 1}: {list}")

main()
