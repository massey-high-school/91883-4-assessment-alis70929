# Quiz Quest Component 1 String Checker v1 (My code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario

def string_check(question, yes_response, no_response):

    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(yes_response)
            print()
            return "yes"
        elif response == "no" or response == "n":
            print(no_response)
            print()
            return "no"
        else:
            print("Please enter Yes/No")


# Main Routine
loop = True
while loop:
    times_table_all = string_check("Would you like to do all 12 times tables at once?",
                                   "You have chosen to practice all times tables at once",
                                   "You have chosen to do a specific times tables")


    continuous = string_check("Would you like to answer questions continuously?",
                              "You have chosen to do questions continuously",
                              "You have chosen to do a specific amount of rounds")
