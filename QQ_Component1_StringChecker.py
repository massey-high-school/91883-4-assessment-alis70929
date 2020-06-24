# Quiz Quest Component 1 String Checker v1 (My code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario

# The Function that checks if a string is valid for yes/no
def string_check(question, yes_response, no_response):

    valid = False
    while not valid:
        # Asks User the question
        response = input(question).lower()
        # Checks if response is yes or y
        if response == "yes" or response == "y":
            # Displays feedback to user
            print(yes_response)
            print()
            # Returns answer as yes to the main code
            return "yes"
        # Checks if response is no or n
        elif response == "no" or response == "n":
            # Displays feedback to user
            print(no_response)
            print()
            # Returns answer as no to the main code
            return "no"
        # If they entered anything other than the above
        else:
            # Tell the user to enter yes or no
            print("Please enter Yes/No")


# Main Routine
# Loop for testing purposes
loop = True
while loop:
    # Asks user if they want to do all 12 times tables at once and puts appropiate feedback into the string checker function
    times_table_all = string_check("Would you like to do all 12 times tables at once?",
                                   "You have chosen to practice all times tables at once",
                                   "You have chosen to do a specific times tables")

    # Asks if they want to answer questions continously and puts appropiate feedback into the string checker function
    continuous = string_check("Would you like to answer questions continuously?",
                              "You have chosen to do questions continuously",
                              "You have chosen to do a specific amount of rounds")
