#get input for plate and call check_valid procedure
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#check if the plate is valid
def is_valid(s):
    #set up a flag variable for finding characters, spaces and numbers, set default to false

    #TODO

    #traverse the string one character at a time by index

    #TODO

        #check for any non-allowable characters

        #TODO

        #check for numeric non-alloable cases (first character = 0 or numbers greater than 999)
        i
        #TODO

        #change flag variables if alpha, space or number character are found

        #TODO

        #if letters and numbers are found, make sure they are separted by a space

        #TODO

        #make sure 7 letters or less if only letters

        #TODO

        #if space found and no letters or number, return invalid
        i
        #TODO

            #else, split string into letters (front part) and numbers (back part)

            #TODO

            #make sure first number not 0

            #TODO

            #verify valid number of letters and numbers

            #TODO

    #if not return flase after iterating through string, return True
    return True

#call main procedure
main()
